from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LocalLLMEngine:
    def __init__(self, model_id="mistralai/Mistral-7B-Instruct-v0.2"):
        print(">>> Loading LLM:", model_id)

        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def generate(self, prompt: str, max_new_tokens=256):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=0.2,
            do_sample=False
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


llm = LocalLLMEngine()
