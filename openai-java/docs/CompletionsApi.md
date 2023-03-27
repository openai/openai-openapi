# CompletionsApi

All URIs are relative to *https://api.openai.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCompletion**](CompletionsApi.md#createCompletion) | **POST** /completions | Create Completion |


<a name="createCompletion"></a>
# **createCompletion**
> CreateCompletionResponse createCompletion(createCompletionRequest)

Create Completion

Creates a completion for the provided prompt and parameters

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.CompletionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    CompletionsApi apiInstance = new CompletionsApi(defaultClient);
    CreateCompletionRequest createCompletionRequest = new CreateCompletionRequest(); // CreateCompletionRequest | 
    try {
      CreateCompletionResponse result = apiInstance.createCompletion(createCompletionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompletionsApi#createCompletion");
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
| **createCompletionRequest** | [**CreateCompletionRequest**](CreateCompletionRequest.md)|  | |

### Return type

[**CreateCompletionResponse**](CreateCompletionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

