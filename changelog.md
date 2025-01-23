# Updates to Admin APIs, Real-time Sessions, and Fine-tuning Request Payloads

1. **New admin API key endpoints**: You can now manage admin-level keys with “GET,” “POST,” “GET by ID,” and “DELETE” calls at `/organization/admin_api_keys`. This makes it easier to create, review, and delete high-permission keys without mixing them up with normal API keys.
2. **New realtime sessions endpoint**: There is now a “POST /realtime/sessions” method for ephemeral token creation. This lets you quickly generate short-lived client tokens to power more dynamic, real-time applications.
Example Payload:
```json
{
    "model": "gpt-4o-realtime-preview-2024-12-17",
    "modalities": ["audio", "text"],
    "instructions": "You are a helpful assistant.",
    "voice": "alloy",
    "input_audio_format": "pcm16",
    "output_audio_format": "pcm16",
    "input_audio_transcription": {
        "model": "whisper-1"
    },
    "turn_detection": null,
    "tools": [],
    "tool_choice": "auto",
    "temperature": 0.8,
    "max_response_output_tokens": "inf"
}
```

3. **Fine-tuning job creation changed**: the request now requires you to nest fields under “method” with “type” and “hyperparameters” inside. The [finetuning UI](https://platform.openai.com/finetune) remains unchanged
```json
{
    "training_file": "file-abc123",
    "model": "gpt-4o-mini",
    "method": {
        "type": "supervised",
        "supervised": {
            "hyperparameters": {
                "n_epochs": 2
            }
        }
    }
}
```

