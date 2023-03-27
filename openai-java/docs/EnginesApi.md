# EnginesApi

All URIs are relative to *https://api.openai.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAnswer**](EnginesApi.md#createAnswer) | **POST** /answers | Create Answer |
| [**createClassification**](EnginesApi.md#createClassification) | **POST** /classifications | Create Classification |
| [**createSearch**](EnginesApi.md#createSearch) | **POST** /engines/{engine_id}/search | Create Search |
| [**listEngines**](EnginesApi.md#listEngines) | **GET** /engines | List Engines |
| [**retrieveEngine**](EnginesApi.md#retrieveEngine) | **GET** /engines/{engine_id} | Retrieve Engine |


<a name="createAnswer"></a>
# **createAnswer**
> CreateAnswerResponse createAnswer(createAnswerRequest)

Create Answer

Answers the specified question using the provided documents and examples.  The endpoint first [searches](/docs/api-reference/searches) over provided documents or files to find relevant context. The relevant context is combined with the provided examples and question to create the prompt for [completion](/docs/api-reference/completions). 

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.EnginesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    EnginesApi apiInstance = new EnginesApi(defaultClient);
    CreateAnswerRequest createAnswerRequest = new CreateAnswerRequest(); // CreateAnswerRequest | 
    try {
      CreateAnswerResponse result = apiInstance.createAnswer(createAnswerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnginesApi#createAnswer");
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
| **createAnswerRequest** | [**CreateAnswerRequest**](CreateAnswerRequest.md)|  | |

### Return type

[**CreateAnswerResponse**](CreateAnswerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="createClassification"></a>
# **createClassification**
> CreateClassificationResponse createClassification(createClassificationRequest)

Create Classification

Classifies the specified &#x60;query&#x60; using provided examples.  The endpoint first [searches](/docs/api-reference/searches) over the labeled examples to select the ones most relevant for the particular query. Then, the relevant examples are combined with the query to construct a prompt to produce the final label via the [completions](/docs/api-reference/completions) endpoint.  Labeled examples can be provided via an uploaded &#x60;file&#x60;, or explicitly listed in the request using the &#x60;examples&#x60; parameter for quick tests and small scale use cases. 

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.EnginesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    EnginesApi apiInstance = new EnginesApi(defaultClient);
    CreateClassificationRequest createClassificationRequest = new CreateClassificationRequest(); // CreateClassificationRequest | 
    try {
      CreateClassificationResponse result = apiInstance.createClassification(createClassificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnginesApi#createClassification");
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
| **createClassificationRequest** | [**CreateClassificationRequest**](CreateClassificationRequest.md)|  | |

### Return type

[**CreateClassificationResponse**](CreateClassificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="createSearch"></a>
# **createSearch**
> CreateSearchResponse createSearch(engineId, createSearchRequest)

Create Search

The search endpoint computes similarity scores between provided query and documents. Documents can be passed directly to the API if there are no more than 200 of them.  To go beyond the 200 document limit, documents can be processed offline and then used for efficient retrieval at query time. When &#x60;file&#x60; is set, the search endpoint searches over all the documents in the given file and returns up to the &#x60;max_rerank&#x60; number of documents. These documents will be returned along with their search scores.  The similarity score is a positive score that usually ranges from 0 to 300 (but can sometimes go higher), where a score above 200 usually means the document is semantically similar to the query. 

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.EnginesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    EnginesApi apiInstance = new EnginesApi(defaultClient);
    String engineId = "davinci"; // String | The ID of the engine to use for this request.  You can select one of `ada`, `babbage`, `curie`, or `davinci`.
    CreateSearchRequest createSearchRequest = new CreateSearchRequest(); // CreateSearchRequest | 
    try {
      CreateSearchResponse result = apiInstance.createSearch(engineId, createSearchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnginesApi#createSearch");
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
| **engineId** | **String**| The ID of the engine to use for this request.  You can select one of &#x60;ada&#x60;, &#x60;babbage&#x60;, &#x60;curie&#x60;, or &#x60;davinci&#x60;. | |
| **createSearchRequest** | [**CreateSearchRequest**](CreateSearchRequest.md)|  | |

### Return type

[**CreateSearchResponse**](CreateSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="listEngines"></a>
# **listEngines**
> ListEnginesResponse listEngines()

List Engines

Lists the currently available (non-finetuned) models, and provides basic information about each one such as the owner and availability.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.EnginesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    EnginesApi apiInstance = new EnginesApi(defaultClient);
    try {
      ListEnginesResponse result = apiInstance.listEngines();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnginesApi#listEngines");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListEnginesResponse**](ListEnginesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="retrieveEngine"></a>
# **retrieveEngine**
> Engine retrieveEngine(engineId)

Retrieve Engine

Retrieves a model instance, providing basic information about it such as the owner and availability.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.EnginesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    EnginesApi apiInstance = new EnginesApi(defaultClient);
    String engineId = "davinci"; // String | The ID of the engine to use for this request 
    try {
      Engine result = apiInstance.retrieveEngine(engineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnginesApi#retrieveEngine");
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
| **engineId** | **String**| The ID of the engine to use for this request  | |

### Return type

[**Engine**](Engine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

