# ImagesApi

All URIs are relative to *https://api.openai.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createImage**](ImagesApi.md#createImage) | **POST** /images/generations | Create Image |
| [**createImageEdit**](ImagesApi.md#createImageEdit) | **POST** /images/edits | Create Image Edit |
| [**createImageVariation**](ImagesApi.md#createImageVariation) | **POST** /images/variations | Create Image Variation |


<a name="createImage"></a>
# **createImage**
> ImagesResponse createImage(createImageRequest)

Create Image

Creates an image given a prompt.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    CreateImageRequest createImageRequest = new CreateImageRequest(); // CreateImageRequest | 
    try {
      ImagesResponse result = apiInstance.createImage(createImageRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#createImage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createImageRequest** | [**CreateImageRequest**](CreateImageRequest.md)|  | |

### Return type

[**ImagesResponse**](ImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="createImageEdit"></a>
# **createImageEdit**
> ImagesResponse createImageEdit(image, prompt, mask, n, size, responseFormat, user)

Create Image Edit

Creates an edited or extended image given an original image and a prompt.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    File image = new File("/path/to/file"); // File | The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask.
    String prompt = "prompt_example"; // String | A text description of the desired image(s). The maximum length is 1000 characters.
    File mask = new File("/path/to/file"); // File | An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where `image` should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as `image`.
    Integer n = 1; // Integer | The number of images to generate. Must be between 1 and 10.
    String size = "256x256"; // String | The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.
    String responseFormat = "url"; // String | The format in which the generated images are returned. Must be one of `url` or `b64_json`.
    String user = "user_example"; // String | A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids). 
    try {
      ImagesResponse result = apiInstance.createImageEdit(image, prompt, mask, n, size, responseFormat, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#createImageEdit");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **image** | **File**| The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask. | |
| **prompt** | **String**| A text description of the desired image(s). The maximum length is 1000 characters. | |
| **mask** | **File**| An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where &#x60;image&#x60; should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as &#x60;image&#x60;. | [optional] |
| **n** | **Integer**| The number of images to generate. Must be between 1 and 10. | [optional] [default to 1] |
| **size** | **String**| The size of the generated images. Must be one of &#x60;256x256&#x60;, &#x60;512x512&#x60;, or &#x60;1024x1024&#x60;. | [optional] [default to 1024x1024] [enum: 256x256, 512x512, 1024x1024] |
| **responseFormat** | **String**| The format in which the generated images are returned. Must be one of &#x60;url&#x60; or &#x60;b64_json&#x60;. | [optional] [default to url] [enum: url, b64_json] |
| **user** | **String**| A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).  | [optional] |

### Return type

[**ImagesResponse**](ImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="createImageVariation"></a>
# **createImageVariation**
> ImagesResponse createImageVariation(image, n, size, responseFormat, user)

Create Image Variation

Creates a variation of a given image.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    File image = new File("/path/to/file"); // File | The image to use as the basis for the variation(s). Must be a valid PNG file, less than 4MB, and square.
    Integer n = 1; // Integer | The number of images to generate. Must be between 1 and 10.
    String size = "256x256"; // String | The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.
    String responseFormat = "url"; // String | The format in which the generated images are returned. Must be one of `url` or `b64_json`.
    String user = "user_example"; // String | A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids). 
    try {
      ImagesResponse result = apiInstance.createImageVariation(image, n, size, responseFormat, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#createImageVariation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **image** | **File**| The image to use as the basis for the variation(s). Must be a valid PNG file, less than 4MB, and square. | |
| **n** | **Integer**| The number of images to generate. Must be between 1 and 10. | [optional] [default to 1] |
| **size** | **String**| The size of the generated images. Must be one of &#x60;256x256&#x60;, &#x60;512x512&#x60;, or &#x60;1024x1024&#x60;. | [optional] [default to 1024x1024] [enum: 256x256, 512x512, 1024x1024] |
| **responseFormat** | **String**| The format in which the generated images are returned. Must be one of &#x60;url&#x60; or &#x60;b64_json&#x60;. | [optional] [default to url] [enum: url, b64_json] |
| **user** | **String**| A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).  | [optional] |

### Return type

[**ImagesResponse**](ImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

