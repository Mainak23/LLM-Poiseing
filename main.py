
from transformers import AutoModelForCausalLM, AutoTokenizer

from model_report import generate_model_report
from tokenizer_report import generate_tokenizer_report


MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"


def main():

    print("Loading model...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME
    )

    print("Generating model report...")

    output_model = generate_model_report(
        model=model,
        model_name="Base Model",
        output_file="model_report.md"
    )

    

    output_tokenize=generate_tokenizer_report(
        tokenizer,
        output_file="tokenizer_report.md"
    )

    print(f"Report created:{output_model}&{output_tokenize}")




if __name__ == "__main__":
    main()
