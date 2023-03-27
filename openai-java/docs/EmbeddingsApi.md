# EmbeddingsApi

All URIs are relative to *https://api.openai.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEmbedding**](EmbeddingsApi.md#createEmbedding) | **POST** /embeddings | Create Embedding |


<a name="createEmbedding"></a>
# **createEmbedding**
> CreateEmbeddingResponse createEmbedding(createEmbeddingRequest)

Create Embedding

Creates an embedding vector representing the input text.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.EmbeddingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    EmbeddingsApi apiInstance = new EmbeddingsApi(defaultClient);
    CreateEmbeddingRequest createEmbeddingRequest = new CreateEmbeddingRequest(); // CreateEmbeddingRequest | 
    try {
      CreateEmbeddingResponse result = apiInstance.createEmbedding(createEmbeddingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbeddingsApi#createEmbedding");
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
| **createEmbeddingRequest** | [**CreateEmbeddingRequest**](CreateEmbeddingRequest.md)|  | |

### Return type

[**CreateEmbeddingResponse**](CreateEmbeddingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

