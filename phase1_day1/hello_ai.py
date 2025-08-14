from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Pick a small model for CPU. You can try "distilgpt2" for faster runs.
model_id = "distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_id)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_id)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

prompt = "AI in cloud computing will"
out = pipe(
    prompt,
    max_new_tokens=120,       # use ONLY this (remove max_length)
    truncation=True,          # fixes the truncation warning
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.2,   # reduces loops/repeated phrases
    no_repeat_ngram_size=3,   # further reduces repetition
    pad_token_id=tokenizer.pad_token_id,
    clean_up_tokenization_spaces=True
)

text = out[0]["generated_text"]
print(text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)
