# FilesApi

All URIs are relative to *https://api.openai.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFile**](FilesApi.md#createFile) | **POST** /files | Create File |
| [**deleteFile**](FilesApi.md#deleteFile) | **DELETE** /files/{file_id} | Delete File |
| [**downloadFile**](FilesApi.md#downloadFile) | **GET** /files/{file_id}/content | Download File |
| [**listFiles**](FilesApi.md#listFiles) | **GET** /files | List Files |
| [**retrieveFile**](FilesApi.md#retrieveFile) | **GET** /files/{file_id} | Retrieve File |


<a name="createFile"></a>
# **createFile**
> OpenAIFile createFile(_file, purpose)

Create File

Upload a file that contains document(s) to be used across various endpoints/features. Currently, the size of all the files uploaded by one organization can be up to 1 GB. Please contact us if you need to increase the storage limit. 

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    FilesApi apiInstance = new FilesApi(defaultClient);
    File _file = new File("/path/to/file"); // File | Name of the [JSON Lines](https://jsonlines.readthedocs.io/en/latest/) file to be uploaded.  If the `purpose` is set to \\\"fine-tune\\\", each line is a JSON record with \\\"prompt\\\" and \\\"completion\\\" fields representing your [training examples](/docs/guides/fine-tuning/prepare-training-data). 
    String purpose = "purpose_example"; // String | The intended purpose of the uploaded documents.  Use \\\"fine-tune\\\" for [Fine-tuning](/docs/api-reference/fine-tunes). This allows us to validate the format of the uploaded file. 
    try {
      OpenAIFile result = apiInstance.createFile(_file, purpose);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#createFile");
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
| **_file** | **File**| Name of the [JSON Lines](https://jsonlines.readthedocs.io/en/latest/) file to be uploaded.  If the &#x60;purpose&#x60; is set to \\\&quot;fine-tune\\\&quot;, each line is a JSON record with \\\&quot;prompt\\\&quot; and \\\&quot;completion\\\&quot; fields representing your [training examples](/docs/guides/fine-tuning/prepare-training-data).  | |
| **purpose** | **String**| The intended purpose of the uploaded documents.  Use \\\&quot;fine-tune\\\&quot; for [Fine-tuning](/docs/api-reference/fine-tunes). This allows us to validate the format of the uploaded file.  | |

### Return type

[**OpenAIFile**](OpenAIFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="deleteFile"></a>
# **deleteFile**
> DeleteFileResponse deleteFile(fileId)

Delete File

Delete a file.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to use for this request
    try {
      DeleteFileResponse result = apiInstance.deleteFile(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#deleteFile");
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
| **fileId** | **String**| The ID of the file to use for this request | |

### Return type

[**DeleteFileResponse**](DeleteFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="downloadFile"></a>
# **downloadFile**
> String downloadFile(fileId)

Download File

Returns the contents of the specified file

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to use for this request
    try {
      String result = apiInstance.downloadFile(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#downloadFile");
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
| **fileId** | **String**| The ID of the file to use for this request | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="listFiles"></a>
# **listFiles**
> ListFilesResponse listFiles()

List Files

Returns a list of files that belong to the user&#39;s organization.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    FilesApi apiInstance = new FilesApi(defaultClient);
    try {
      ListFilesResponse result = apiInstance.listFiles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#listFiles");
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

[**ListFilesResponse**](ListFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="retrieveFile"></a>
# **retrieveFile**
> OpenAIFile retrieveFile(fileId)

Retrieve File

Returns information about a specific file.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The ID of the file to use for this request
    try {
      OpenAIFile result = apiInstance.retrieveFile(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#retrieveFile");
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
| **fileId** | **String**| The ID of the file to use for this request | |

### Return type

[**OpenAIFile**](OpenAIFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

