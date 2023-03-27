# AudioApi

All URIs are relative to *https://api.openai.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTranscription**](AudioApi.md#createTranscription) | **POST** /audio/transcriptions | Create Transcription |
| [**createTranslation**](AudioApi.md#createTranslation) | **POST** /audio/translations | Create Translation |


<a name="createTranscription"></a>
# **createTranscription**
> CreateTranscriptionResponse createTranscription(_file, model, prompt, responseFormat, temperature, language)

Create Transcription

Transcribes audio into the input language.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    AudioApi apiInstance = new AudioApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The audio file to transcribe, in one of these formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm. 
    String model = "model_example"; // String | ID of the model to use. Only `whisper-1` is currently available. 
    String prompt = "prompt_example"; // String | An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should match the audio language. 
    String responseFormat = "json"; // String | The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt. 
    BigDecimal temperature = new BigDecimal("0"); // BigDecimal | The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit. 
    String language = "language_example"; // String | The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency. 
    try {
      CreateTranscriptionResponse result = apiInstance.createTranscription(_file, model, prompt, responseFormat, temperature, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#createTranscription");
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
| **_file** | **File**| The audio file to transcribe, in one of these formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm.  | |
| **model** | **String**| ID of the model to use. Only &#x60;whisper-1&#x60; is currently available.  | |
| **prompt** | **String**| An optional text to guide the model&#39;s style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should match the audio language.  | [optional] |
| **responseFormat** | **String**| The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt.  | [optional] [default to json] |
| **temperature** | **BigDecimal**| The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.  | [optional] [default to 0] |
| **language** | **String**| The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.  | [optional] |

### Return type

[**CreateTranscriptionResponse**](CreateTranscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a name="createTranslation"></a>
# **createTranslation**
> CreateTranslationResponse createTranslation(_file, model, prompt, responseFormat, temperature)

Create Translation

Translates audio into into English.

### Example
```java
// Import classes:
import space.fraktured.ai.client.ApiClient;
import space.fraktured.ai.client.ApiException;
import space.fraktured.ai.client.Configuration;
import space.fraktured.ai.client.models.*;
import space.fraktured.ai.client.api.AudioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openai.com/v1");

    AudioApi apiInstance = new AudioApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The audio file to translate, in one of these formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm. 
    String model = "model_example"; // String | ID of the model to use. Only `whisper-1` is currently available. 
    String prompt = "prompt_example"; // String | An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should be in English. 
    String responseFormat = "json"; // String | The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt. 
    BigDecimal temperature = new BigDecimal("0"); // BigDecimal | The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit. 
    try {
      CreateTranslationResponse result = apiInstance.createTranslation(_file, model, prompt, responseFormat, temperature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudioApi#createTranslation");
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
| **_file** | **File**| The audio file to translate, in one of these formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm.  | |
| **model** | **String**| ID of the model to use. Only &#x60;whisper-1&#x60; is currently available.  | |
| **prompt** | **String**| An optional text to guide the model&#39;s style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should be in English.  | [optional] |
| **responseFormat** | **String**| The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt.  | [optional] [default to json] |
| **temperature** | **BigDecimal**| The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.  | [optional] [default to 0] |

### Return type

[**CreateTranslationResponse**](CreateTranslationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

