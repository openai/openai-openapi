# ModelsApi

All URIs are relative to *https://api.openai.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteModel**](ModelsApi.md#deleteModel) | **DELETE** /models/{model} | Delete Model |
| [**listModels**](ModelsApi.md#listModels) | **GET** /models | List Models |
| [**retrieveModel**](ModelsApi.md#retrieveModel) | **GET** /models/{model} | Retrieve Model |


<a name="deleteModel"></a>
# **deleteModel**
> DeleteModelResponse deleteModel(model)

Delete Model

Delete a fine-tuned model. You must have the Owner role in your organization.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.ModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    ModelsApi apiInstance = new ModelsApi(defaultClient);
    String model = "curie:ft-acmeco-2021-03-03-21-44-20"; // String | The model to delete
    try {
      DeleteModelResponse result = apiInstance.deleteModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelsApi#deleteModel");
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
| **model** | **String**| The model to delete | |

### Return type

[**DeleteModelResponse**](DeleteModelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="listModels"></a>
# **listModels**
> ListModelsResponse listModels()

List Models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.ModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    ModelsApi apiInstance = new ModelsApi(defaultClient);
    try {
      ListModelsResponse result = apiInstance.listModels();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelsApi#listModels");
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

[**ListModelsResponse**](ListModelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="retrieveModel"></a>
# **retrieveModel**
> Model retrieveModel(model)

Retrieve Model

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.ModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    ModelsApi apiInstance = new ModelsApi(defaultClient);
    String model = "text-davinci-001"; // String | The ID of the model to use for this request
    try {
      Model result = apiInstance.retrieveModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelsApi#retrieveModel");
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
| **model** | **String**| The ID of the model to use for this request | |

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

