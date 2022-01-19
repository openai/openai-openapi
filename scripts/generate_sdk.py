import argparse
import os
import sys
import yaml


class NoAliasDumper(yaml.Dumper):
    """
    Yaml aliases (variables prefixed with & and *) are invalid in OpenAPI
    syntax. This custom dumper will expand out all of the aliases when
    dumping the yaml into the sanitized spec file.
    """

    def ignore_aliases(self, data):
        return True


def filter_out_oai_keys(obj):
    """Filter out any custom keys that start with 'oai'."""
    oai_keys = []
    for key in obj:
        if key.startswith("oai"):
            oai_keys.append(key)
    for oai_key in oai_keys:
        del obj[oai_key]


def fix_default_null(obj):
    """
    For some reason openapi-generator fails when properties of type 'object'
    or 'array' have a default value of null, so rewrite those defaults to {}
    and [] respectively (generated code, at least for Typescript, doesn't use
    the defaults anyways).
    """
    if "default" in obj and obj["default"] is None:
        if obj.get("type") == "object":
            obj["default"] = {}
        elif obj.get("type") == "array":
            obj["default"] = []


def fix_nested_array(obj):
    """
    openapi-generator has a bug where it doesn't go past the first level of
    array nesting, so instead of outputting something like Array<Array<string>>>,
    it will just output Array<Array> (which is problematic for Typescript).
    This is a non-ideal hack to set the items of the top-level array to {},
    which will output as Array<any>.
    """
    if obj.get("type") == "array" and obj.get("items", {}).get("type") == "array":
        obj["items"] = {}


def sanitize_spec_object(obj):
    """
    Recursively iterate through the given spec and perform any necessary
    rewrites/sanitization for the spec that will be used to generate SDKs.
    """
    if type(obj) is dict:
        filter_out_oai_keys(obj)
        fix_default_null(obj)
        fix_nested_array(obj)
        for item in obj.values():
            sanitize_spec_object(item)
    elif type(obj) is list:
        for item in obj:
            sanitize_spec_object(item)


def generate_sanitized_spec(sanitized_spec_path):
    """
    Create a sanitized version of the publicly available spec that can be used
    to generate SDKs.
    """
    input_path = os.path.join(os.path.dirname(
        __file__), "../openapi.yaml")
    with open(input_path, "r") as input_file:
        spec = yaml.safe_load(input_file)
        sanitize_spec_object(spec)
        with open(sanitized_spec_path, "w") as output_file:
            yaml.dump(spec, output_file, Dumper=NoAliasDumper, sort_keys=False)


def generate_sdk(sanitized_spec_path, sdk_type, output_path):
    """Use openapi-generator to generate the SDK."""
    if sdk_type == "node":
        template_override_path = os.path.join(os.path.dirname(
            __file__), "../sdk-template-overrides/typescript-axios")
        os.system(
            f"openapi-generator generate -i {sanitized_spec_path} -g typescript-axios -o {output_path} -p supportsES6=true -t {template_override_path}")
    else:
        print(f"Unsupported SDK type {sdk_type}, skipping SDK generation")


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sdk", help="sdk type (supported types: 'node')")
parser.add_argument(
    "-o", "--output", help="output directory for the generated sdk")

if __name__ == "__main__":
    args = parser.parse_args()
    if args.sdk is None:
        print("Use -s to specify the SDK type")
        sys.exit(1)
    if args.output is None:
        print("Use -o to specify the output directory")
        sys.exit(1)

    sanitized_spec_path = os.path.join(os.path.dirname(
        __file__), "openapi-sanitized-tmp.yaml")
    print("Generating sanitized spec file...")
    generate_sanitized_spec(sanitized_spec_path)
    print(f"Generating {args.sdk} SDK...")
    generate_sdk(sanitized_spec_path, args.sdk, args.output)
    print("Deleting sanitized spec file...")
    os.remove(sanitized_spec_path)
