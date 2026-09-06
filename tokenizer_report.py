def generate_tokenizer_report(
    tokenizer,
    output_file="tokenizer_report.md"
):
    report = []

    report.append("# Tokenizer Report\n")

    # ============================================================
    # Basic Information
    # ============================================================

    report.append("## 1. Basic Information\n")

    report.append("| Property | Value |")
    report.append("|---|---|")

    report.append(
        f"| Tokenizer Class | `{type(tokenizer).__name__}` |"
    )

    report.append(
        f"| Vocabulary Size | `{len(tokenizer):,}` |"
    )

    report.append(
        f"| Chat Template Type | `{type(tokenizer.chat_template).__name__}` |"
    )

    report.append(
        f"| Chat Template Exists | `{tokenizer.chat_template is not None}` |"
    )

    # ============================================================
    # Special Tokens
    # ============================================================

    report.append("\n## 2. Special Tokens\n")

    special_tokens = [
        "bos_token",
        "eos_token",
        "unk_token",
        "pad_token",
        "sep_token",
        "cls_token",
        "mask_token",
    ]

    report.append("| Token | Value | Token ID |")
    report.append("|---|---|---:|")

    for token_name in special_tokens:

        token = getattr(tokenizer, token_name, None)

        if token is not None:
            token_id = tokenizer.convert_tokens_to_ids(token)

            report.append(
                f"| `{token_name}` | `{token}` | `{token_id}` |"
            )

    # ============================================================
    # Chat Template
    # ============================================================

    report.append("\n## 3. Chat Template\n")

    if tokenizer.chat_template is not None:

        report.append(
            "The tokenizer contains a chat template used to convert "
            "structured messages such as system/user/assistant messages "
            "into the text format expected by the model."
        )

        report.append("\n### Template\n")

        report.append("```jinja2")
        report.append(str(tokenizer.chat_template))
        report.append("```")

    else:

        report.append(
            "No chat template is defined for this tokenizer."
        )

    # ============================================================
    # Tokenizer Configuration
    # ============================================================

    report.append("\n## 4. Tokenizer Configuration\n")

    tokenizer_config = tokenizer.init_kwargs

    report.append("| Configuration | Value |")
    report.append("|---|---|")

    for key, value in tokenizer_config.items():

        value = str(value).replace("|", "\\|").replace("\n", " ")

        report.append(
            f"| `{key}` | `{value}` |"
        )

    # ============================================================
    # Save
    # ============================================================

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("\n".join(report))

    return output_file
