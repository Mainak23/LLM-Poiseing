import torch
import torch.nn as nn


def generate_model_report(
    model,
    model_name="Model",
    output_file="model_report.md"
):
    """
    Generate a human-friendly Markdown report for a Hugging Face model.

    The report automatically adapts to the model architecture instead of
    assuming fields such as num_key_value_heads, head_dim, RoPE, etc.
    """

    config = model.config
    report = []

    # ============================================================
    # Helper
    # ============================================================

    def format_value(value):
        """Convert Python/model values into Markdown-friendly text."""
        if value is None:
            return "N/A"

        value = str(value)

        # Prevent Markdown tables from breaking
        value = value.replace("|", "\\|")
        value = value.replace("\n", " ")

        return value

    # ============================================================
    # Header
    # ============================================================

    report.append(f"# {model_name} — Model Report\n")

    report.append(
        "> Automatically generated model architecture and parameter report."
    )

    # ============================================================
    # 1. Basic Model Information
    # ============================================================

    report.append("\n## 1. Basic Model Information\n")

    model_class = type(model).__name__

    architectures = getattr(config, "architectures", None)

    basic_info = [
        ("Model Class", model_class),
        ("Model Type", getattr(config, "model_type", None)),
        ("Architecture", architectures),
        ("Vocabulary Size", getattr(config, "vocab_size", None)),
        ("Hidden Size", getattr(config, "hidden_size", None)),
        ("Intermediate Size", getattr(config, "intermediate_size", None)),
        ("Number of Layers", getattr(config, "num_hidden_layers", None)),
        ("Attention Heads", getattr(config, "num_attention_heads", None)),
        ("KV Heads", getattr(config, "num_key_value_heads", None)),
        ("Head Dimension", getattr(config, "head_dim", None)),
        (
            "Maximum Position Embeddings",
            getattr(config, "max_position_embeddings", None)
        ),
        ("Activation Function", getattr(config, "hidden_act", None)),
        ("RMS Norm Epsilon", getattr(config, "rms_norm_eps", None)),
        ("RoPE Theta", getattr(config, "rope_theta", None)),
        ("RoPE Parameters", getattr(config, "rope_parameters", None)),
        ("Torch Data Type", getattr(config, "torch_dtype", None)),
        (
            "Tie Word Embeddings",
            getattr(config, "tie_word_embeddings", None)
        ),
    ]

    report.append("| Property | Value |")
    report.append("|---|---|")

    for name, value in basic_info:

        if value is not None:
            report.append(
                f"| **{name}** | `{format_value(value)}` |"
            )

    # ============================================================
    # 2. Parameter Information
    # ============================================================

    report.append("\n## 2. Parameter Information\n")

    total_params = sum(
        parameter.numel()
        for parameter in model.parameters()
    )

    trainable_params = sum(
        parameter.numel()
        for parameter in model.parameters()
        if parameter.requires_grad
    )

    frozen_params = total_params - trainable_params

    trainable_percentage = (
        (trainable_params / total_params) * 100
        if total_params > 0
        else 0
    )

    report.append("| Parameter Information | Value |")
    report.append("|---|---:|")

    report.append(
        f"| Total Parameters | `{total_params:,}` |"
    )

    report.append(
        f"| Trainable Parameters | `{trainable_params:,}` |"
    )

    report.append(
        f"| Frozen Parameters | `{frozen_params:,}` |"
    )

    report.append(
        f"| Trainable Percentage | `{trainable_percentage:.4f}%` |"
    )

    # ============================================================
    # 3. Model Data Types
    # ============================================================

    report.append("\n## 3. Model Data Types\n")

    dtype_counts = {}

    for parameter in model.parameters():

        dtype = str(parameter.dtype)

        dtype_counts[dtype] = (
            dtype_counts.get(dtype, 0)
            + parameter.numel()
        )

    report.append("| Data Type | Parameters |")
    report.append("|---|---:|")

    for dtype, count in dtype_counts.items():

        report.append(
            f"| `{dtype}` | `{count:,}` |"
        )

    # ============================================================
    # 4. Device Information
    # ============================================================

    report.append("\n## 4. Device Information\n")

    device_counts = {}

    for parameter in model.parameters():

        device = str(parameter.device)

        device_counts[device] = (
            device_counts.get(device, 0)
            + parameter.numel()
        )

    report.append("| Device | Parameters |")
    report.append("|---|---:|")

    for device, count in device_counts.items():

        report.append(
            f"| `{device}` | `{count:,}` |"
        )

    # ============================================================
    # 5. Parameter Memory Estimate
    # ============================================================

    report.append("\n## 5. Parameter Memory Estimate\n")

    dtype_size = {
        torch.float32: 4,
        torch.float16: 2,
        torch.bfloat16: 2,
        torch.float64: 8,
        torch.int8: 1,
        torch.uint8: 1,
        torch.int16: 2,
        torch.int32: 4,
        torch.int64: 8,
    }

    estimated_bytes = 0

    for parameter in model.parameters():

        bytes_per_element = dtype_size.get(
            parameter.dtype,
            0
        )

        estimated_bytes += (
            parameter.numel()
            * bytes_per_element
        )

    estimated_mb = estimated_bytes / (1024 ** 2)
    estimated_gb = estimated_bytes / (1024 ** 3)

    report.append(
        f"- **Estimated parameter memory:** "
        f"`{estimated_mb:,.2f} MB`"
    )

    report.append(
        f"- **Estimated parameter memory:** "
        f"`{estimated_gb:,.2f} GB`"
    )

    report.append(
        "> Note: This is an estimate based on parameter dtype. "
        "Actual GPU/CPU memory usage can be higher because of "
        "activations, gradients, optimizer states, KV cache, "
        "quantization metadata, and framework overhead."
    )

    # ============================================================
    # 6. Embedding Layers
    # ============================================================

    report.append("\n## 6. Embedding Layers\n")

    embedding_found = False

    report.append("| Layer | Shape |")
    report.append("|---|---|")

    for name, module in model.named_modules():

        if isinstance(module, nn.Embedding):

            embedding_found = True

            report.append(
                f"| `{name}` | `{tuple(module.weight.shape)}` |"
            )

    if not embedding_found:

        report.append(
            "| No standard `nn.Embedding` layer found | - |"
        )

    # ============================================================
    # 7. Linear Layers
    # ============================================================

    report.append("\n## 7. Linear Layers\n")

    linear_layers = []

    for name, module in model.named_modules():

        if isinstance(module, nn.Linear):

            linear_layers.append(
                (
                    name,
                    tuple(module.weight.shape),
                    module.weight.dtype
                )
            )

    report.append("| Layer | Weight Shape | Data Type |")
    report.append("|---|---|---|")

    if linear_layers:

        for name, shape, dtype in linear_layers:

            report.append(
                f"| `{name}` | `{shape}` | `{dtype}` |"
            )

    else:

        report.append(
            "| No standard `nn.Linear` layers found | - | - |"
        )

    # ============================================================
    # 8. LoRA Candidate Layers
    # ============================================================

    report.append("\n## 8. Potential LoRA Target Layers\n")

    report.append(
        "The following common layer names are often considered "
        "when selecting LoRA targets."
    )

    common_lora_targets = [
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
        "query",
        "key",
        "value",
        "dense",
    ]

    detected_targets = []

    for name, module in model.named_modules():

        if isinstance(module, nn.Linear):

            layer_name = name.split(".")[-1]

            if layer_name in common_lora_targets:

                detected_targets.append(name)

    if detected_targets:

        report.append("\n### Detected Candidate Layers\n")

        for name in detected_targets:

            report.append(f"- `{name}`")

    else:

        report.append(
            "\nNo common LoRA target names were automatically detected."
        )

    report.append(
        "\n> These are only candidates. Actual LoRA targets should be "
        "selected based on the model architecture."
    )

    # ============================================================
    # 9. Complete Hugging Face Configuration
    # ============================================================

    report.append("\n## 9. Complete Model Configuration\n")

    report.append(
        "This section contains the configuration fields actually "
        "present in the model. Architecture-specific fields are "
        "included automatically."
    )

    config_dict = config.to_dict()

    report.append("\n| Configuration | Value |")
    report.append("|---|---|")

    for key, value in config_dict.items():

        report.append(
            f"| `{key}` | `{format_value(value)}` |"
        )

    # ============================================================
    # 10. Human-Friendly Explanation
    # ============================================================

    report.append("\n## 10. Human-Friendly Explanation\n")

    report.append("""
### Model Type

Identifies the general model architecture used by the Hugging Face
configuration, for example `llama`, `mistral`, `qwen2`, or another
architecture.

### Vocabulary Size

The vocabulary size is the number of tokens the tokenizer/model can
represent. A token can be a complete word, part of a word, punctuation,
or another symbol.

### Hidden Size

The hidden size is the width of the model's internal representation.
Every token is represented internally using vectors of approximately
this size.

A larger hidden size generally provides more representational capacity,
but it also increases memory usage and computation.

### Intermediate Size

The intermediate size is commonly used inside the Transformer
feed-forward network.

The model usually expands the hidden representation to this larger
dimension, applies an activation function, and then projects it back.

### Number of Layers

The number of Transformer layers represents the depth of the model.

Each layer performs additional processing on the token representations.

More layers generally mean a more computationally expensive model.

### Attention Heads

Attention heads allow the model to examine different relationships
between tokens in parallel.

Different attention heads can learn different patterns.

### KV Heads

Some architectures use a separate number of Key/Value heads.

When KV heads are fewer than attention heads, the model may be using
Grouped Query Attention (GQA), which can reduce KV-cache memory usage.

This field does not exist in every architecture.

### Head Dimension

The head dimension represents the size of each attention head.

For many Transformer architectures:

`Hidden Size = Attention Heads × Head Dimension`

However, this relationship can vary depending on the architecture,
so it should not be assumed universally.

### Maximum Position Embeddings

This describes the maximum sequence length associated with the model's
position-encoding configuration.

Modern architectures may implement positional information differently,
so this field may not exist or may not tell the complete story.

### Activation Function

The activation function introduces non-linearity into the neural
network.

Common examples include:

- GELU
- SiLU
- ReLU

Without non-linear activation functions, the network would have much
less ability to learn complex relationships.

### RMS Norm Epsilon

A small numerical-stability value used by architectures that use RMS
normalization.

This field is architecture-specific and therefore may not exist.

### RoPE

RoPE stands for Rotary Position Embedding.

It is one technique used by Transformer models to encode information
about token positions.

Not every model exposes the same RoPE configuration fields.

### Data Type

The model's data type determines how each parameter is represented.

Common examples include:

- `float32`
- `float16`
- `bfloat16`
- `int8`

Lower-precision formats can significantly reduce memory requirements.

### Device

The device tells us where model parameters are stored.

Examples:

- `cpu`
- `cuda:0`
- `cuda:1`

This is important when working with large models because GPU memory
often determines whether the model can be loaded or trained.

### Trainable Parameters

Trainable parameters are the parameters that will be updated during
training.

During standard LoRA fine-tuning, the original model parameters are
usually frozen while the LoRA parameters remain trainable.

This can dramatically reduce the number of parameters that need to be
updated.

### Linear Layers

Linear layers contain weight matrices that perform learned
transformations.

Transformer models contain many important Linear layers.

Common examples include:

- `q_proj`
- `k_proj`
- `v_proj`
- `o_proj`
- `gate_proj`
- `up_proj`
- `down_proj`

These layers are frequently considered when applying LoRA.

### Why Architecture-Specific Fields Matter

Different LLM architectures are not identical.

For example, one model may expose:

`num_key_value_heads`

while another model may not.

Similarly, one architecture may expose:

`rope_theta`

while another may use a different positional-encoding mechanism.

Therefore, a model inspection tool should discover available
configuration fields rather than assuming that every LLM has the same
architecture.
""")

    # ============================================================
    # 11. Architecture Summary
    # ============================================================

    report.append("\n## 11. Architecture Summary\n")

    hidden_size = getattr(config, "hidden_size", None)
    num_heads = getattr(config, "num_attention_heads", None)
    head_dim = getattr(config, "head_dim", None)

    if hidden_size and num_heads and head_dim:

        expected_hidden_size = num_heads * head_dim

        if hidden_size == expected_hidden_size:

            report.append(
                "✅ Attention dimensions are consistent: "
                f"`{hidden_size} = {num_heads} × {head_dim}`"
            )

        else:

            report.append(
                "⚠️ Attention dimensions do not follow the simple "
                "relationship `hidden_size = num_attention_heads × "
                "head_dim`. This may be intentional for the architecture."
            )

    else:

        report.append(
            "Attention dimension consistency could not be calculated "
            "because the required fields are not available."
        )

    # ============================================================
    # 12. Layer 0 Structure
    # ============================================================

    report.append("\n## 12. First Transformer Layer Structure\n")

    layer_zero = None

    # Try common Hugging Face structures
    possible_layer_paths = [
        "model.layers",
        "transformer.h",
        "encoder.layer",
        "layers",
    ]

    for path in possible_layer_paths:

        current = model

        try:

            for part in path.split("."):

                current = getattr(current, part)

            if len(current) > 0:

                layer_zero = current[0]
                break

        except (AttributeError, TypeError, IndexError):

            continue

    if layer_zero is not None:

        report.append("```text")

        report.append(
            str(layer_zero)
        )

        report.append("```")

    else:

        report.append(
            "The first Transformer layer could not be automatically "
            "identified for this architecture."
        )

    # ============================================================
    # 13. Report Footer
    # ============================================================

    report.append("\n---\n")

    report.append(
        "*Report generated automatically using the Hugging Face model "
        "object.*"
    )

    # ============================================================
    # Write Markdown File
    # ============================================================

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("\n".join(report))

    return output_file
