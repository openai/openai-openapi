# EditsApi

All URIs are relative to *https://api.openai.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEdit**](EditsApi.md#createEdit) | **POST** /edits | Create Edit |


<a name="createEdit"></a>
# **createEdit**
> CreateEditResponse createEdit(createEditRequest)

Create Edit

Creates a new edit for the provided input, instruction, and parameters.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.EditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    EditsApi apiInstance = new EditsApi(defaultClient);
    CreateEditRequest createEditRequest = new CreateEditRequest(); // CreateEditRequest | 
    try {
      CreateEditResponse result = apiInstance.createEdit(createEditRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsApi#createEdit");
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
| **createEditRequest** | [**CreateEditRequest**](CreateEditRequest.md)|  | |

### Return type

[**CreateEditResponse**](CreateEditResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

