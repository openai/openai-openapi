# OpenAI Fine-tuning Guide

## Overview
Fine-tuning allows you to customize OpenAI's models for specific use cases by training them on your own data([1](https://platform.openai.com/docs/guides/fine-tuning)). This is particularly useful for:

- Setting specific style, tone, or format
- Improving reliability for desired outputs
- Handling complex prompts and edge cases
- Teaching new skills or tasks

## Currently Available Models

- `gpt-4o-mini` (recommended for most users)
- `gpt-3.5-turbo` 
- `babbage-002`
- `davinci-002`

Note: GPT-4 fine-tuning is currently in experimental access([1](https://platform.openai.com/docs/guides/fine-tuning)).

## Step-by-Step Guide

### 1. Prepare Your Dataset

Create a JSONL file with your training examples. Each example should be a conversation in this format:

```jsonl
{"messages": [
    {"role": "system", "content": "System message here"},
    {"role": "user", "content": "User message here"},
    {"role": "assistant", "content": "Assistant response here"}
]}
```

Best practices:
- Include at least 10 examples
- Make examples diverse and representative
- Target specific cases where the base model isn't performing as desired
- Include ideal responses in the assistant messages

### 2. Validate and Upload Your Data

```python
from openai import OpenAI
client = OpenAI()

# Upload the training file
file = client.files.create(
    file=open("training_data.jsonl", "rb"),
    purpose="fine-tune"
)
```

### 3. Create Fine-tuning Job

Based on the recent changelog, use this updated format:

```python
client.fine_tuning.jobs.create(
    training_file="file-abc123",
    model="gpt-3.5-turbo",
    method={
        "type": "supervised",
        "supervised": {
            "hyperparameters": {
                "n_epochs": 2
            }
        }
    }
)
```

### 4. Configure Hyperparameters (Optional)

Key hyperparameters to consider:
- `n_epochs`: Increase by 1-2 if model isn't following training data enough
- Decrease epochs if model becomes less diverse than desired
- Adjust learning rate if model isn't converging

### 5. Monitor Training Progress

```python
# Get the status of your fine-tuning job
job = client.fine_tuning.jobs.retrieve("job-id")
print(job.status)
```

## Cost Considerations

- Fine-tuning costs vary based on model and data size
- Training tokens and usage tokens have different pricing
- Consider testing with a smaller dataset first

## Best Practices

1. **Start Simple**: Begin with base model prompt engineering before fine-tuning
2. **Quality Data**: Ensure training data is high-quality and well-formatted
3. **Test Thoroughly**: Compare fine-tuned model against base model using test cases
4. **Iterate**: Monitor performance and adjust hyperparameters as needed

## Rate Limits

- Fine-tuned models share rate limits with their base models
- For example, if you use 50% of `gpt-3.5-turbo`'s TPM limit, your fine-tuned version will only have the remaining 50% available

## Evaluation

To evaluate your fine-tuned model:
1. Generate samples from both base and fine-tuned models
2. Compare responses side-by-side
3. Consider using OpenAI's evals framework for comprehensive testing

Remember that fine-tuning can be complementary to retrieval strategies - they're not mutually exclusive approaches to improving model performance.
