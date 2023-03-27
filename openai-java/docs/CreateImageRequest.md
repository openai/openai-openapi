

# CreateImageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**prompt** | **String** | A text description of the desired image(s). The maximum length is 1000 characters. |  |
|**n** | **Integer** | The number of images to generate. Must be between 1 and 10. |  [optional] |
|**size** | [**SizeEnum**](#SizeEnum) | The size of the generated images. Must be one of &#x60;256x256&#x60;, &#x60;512x512&#x60;, or &#x60;1024x1024&#x60;. |  [optional] |
|**responseFormat** | [**ResponseFormatEnum**](#ResponseFormatEnum) | The format in which the generated images are returned. Must be one of &#x60;url&#x60; or &#x60;b64_json&#x60;. |  [optional] |
|**user** | **String** | A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).  |  [optional] |



## Enum: SizeEnum

| Name | Value |
|---- | -----|
| _256X256 | &quot;256x256&quot; |
| _512X512 | &quot;512x512&quot; |
| _1024X1024 | &quot;1024x1024&quot; |



## Enum: ResponseFormatEnum

| Name | Value |
|---- | -----|
| URL | &quot;url&quot; |
| B64_JSON | &quot;b64_json&quot; |



