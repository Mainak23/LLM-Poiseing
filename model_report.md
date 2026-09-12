# Base Model — Model Report

> Automatically generated model architecture and parameter report.

## 1. Basic Model Information

| Property | Value |
|---|---|
| **Model Class** | `LlamaForCausalLM` |
| **Model Type** | `llama` |
| **Architecture** | `['LlamaForCausalLM']` |
| **Vocabulary Size** | `128256` |
| **Hidden Size** | `2048` |
| **Intermediate Size** | `8192` |
| **Number of Layers** | `16` |
| **Attention Heads** | `32` |
| **KV Heads** | `8` |
| **Head Dimension** | `64` |
| **Maximum Position Embeddings** | `131072` |
| **Activation Function** | `silu` |
| **RMS Norm Epsilon** | `1e-05` |
| **RoPE Parameters** | `{'factor': 32.0, 'high_freq_factor': 4.0, 'low_freq_factor': 1.0, 'original_max_position_embeddings': 8192, 'rope_type': 'llama3', 'rope_theta': 500000.0}` |
| **Torch Data Type** | `bfloat16` |
| **Tie Word Embeddings** | `True` |

## 2. Parameter Information

| Parameter Information | Value |
|---|---:|
| Total Parameters | `1,235,814,400` |
| Trainable Parameters | `1,235,814,400` |
| Frozen Parameters | `0` |
| Trainable Percentage | `100.0000%` |

## 3. Model Data Types

| Data Type | Parameters |
|---|---:|
| `torch.bfloat16` | `1,235,814,400` |

## 4. Device Information

| Device | Parameters |
|---|---:|
| `cpu` | `1,235,814,400` |

## 5. Parameter Memory Estimate

- **Estimated parameter memory:** `2,357.13 MB`
- **Estimated parameter memory:** `2.30 GB`
> Note: This is an estimate based on parameter dtype. Actual GPU/CPU memory usage can be higher because of activations, gradients, optimizer states, KV cache, quantization metadata, and framework overhead.

## 6. Embedding Layers

| Layer | Shape |
|---|---|
| `model.embed_tokens` | `(128256, 2048)` |

## 7. Linear Layers

| Layer | Weight Shape | Data Type |
|---|---|---|
| `model.layers.0.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.0.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.0.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.0.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.0.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.0.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.0.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.1.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.1.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.1.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.1.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.1.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.1.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.1.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.2.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.2.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.2.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.2.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.2.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.2.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.2.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.3.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.3.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.3.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.3.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.3.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.3.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.3.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.4.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.4.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.4.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.4.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.4.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.4.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.4.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.5.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.5.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.5.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.5.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.5.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.5.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.5.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.6.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.6.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.6.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.6.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.6.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.6.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.6.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.7.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.7.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.7.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.7.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.7.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.7.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.7.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.8.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.8.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.8.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.8.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.8.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.8.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.8.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.9.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.9.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.9.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.9.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.9.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.9.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.9.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.10.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.10.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.10.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.10.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.10.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.10.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.10.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.11.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.11.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.11.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.11.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.11.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.11.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.11.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.12.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.12.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.12.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.12.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.12.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.12.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.12.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.13.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.13.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.13.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.13.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.13.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.13.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.13.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.14.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.14.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.14.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.14.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.14.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.14.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.14.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `model.layers.15.self_attn.q_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.15.self_attn.k_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.15.self_attn.v_proj` | `(512, 2048)` | `torch.bfloat16` |
| `model.layers.15.self_attn.o_proj` | `(2048, 2048)` | `torch.bfloat16` |
| `model.layers.15.mlp.gate_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.15.mlp.up_proj` | `(8192, 2048)` | `torch.bfloat16` |
| `model.layers.15.mlp.down_proj` | `(2048, 8192)` | `torch.bfloat16` |
| `lm_head` | `(128256, 2048)` | `torch.bfloat16` |

## 8. Potential LoRA Target Layers

The following common layer names are often considered when selecting LoRA targets.

### Detected Candidate Layers

- `model.layers.0.self_attn.q_proj`
- `model.layers.0.self_attn.k_proj`
- `model.layers.0.self_attn.v_proj`
- `model.layers.0.self_attn.o_proj`
- `model.layers.0.mlp.gate_proj`
- `model.layers.0.mlp.up_proj`
- `model.layers.0.mlp.down_proj`
- `model.layers.1.self_attn.q_proj`
- `model.layers.1.self_attn.k_proj`
- `model.layers.1.self_attn.v_proj`
- `model.layers.1.self_attn.o_proj`
- `model.layers.1.mlp.gate_proj`
- `model.layers.1.mlp.up_proj`
- `model.layers.1.mlp.down_proj`
- `model.layers.2.self_attn.q_proj`
- `model.layers.2.self_attn.k_proj`
- `model.layers.2.self_attn.v_proj`
- `model.layers.2.self_attn.o_proj`
- `model.layers.2.mlp.gate_proj`
- `model.layers.2.mlp.up_proj`
- `model.layers.2.mlp.down_proj`
- `model.layers.3.self_attn.q_proj`
- `model.layers.3.self_attn.k_proj`
- `model.layers.3.self_attn.v_proj`
- `model.layers.3.self_attn.o_proj`
- `model.layers.3.mlp.gate_proj`
- `model.layers.3.mlp.up_proj`
- `model.layers.3.mlp.down_proj`
- `model.layers.4.self_attn.q_proj`
- `model.layers.4.self_attn.k_proj`
- `model.layers.4.self_attn.v_proj`
- `model.layers.4.self_attn.o_proj`
- `model.layers.4.mlp.gate_proj`
- `model.layers.4.mlp.up_proj`
- `model.layers.4.mlp.down_proj`
- `model.layers.5.self_attn.q_proj`
- `model.layers.5.self_attn.k_proj`
- `model.layers.5.self_attn.v_proj`
- `model.layers.5.self_attn.o_proj`
- `model.layers.5.mlp.gate_proj`
- `model.layers.5.mlp.up_proj`
- `model.layers.5.mlp.down_proj`
- `model.layers.6.self_attn.q_proj`
- `model.layers.6.self_attn.k_proj`
- `model.layers.6.self_attn.v_proj`
- `model.layers.6.self_attn.o_proj`
- `model.layers.6.mlp.gate_proj`
- `model.layers.6.mlp.up_proj`
- `model.layers.6.mlp.down_proj`
- `model.layers.7.self_attn.q_proj`
- `model.layers.7.self_attn.k_proj`
- `model.layers.7.self_attn.v_proj`
- `model.layers.7.self_attn.o_proj`
- `model.layers.7.mlp.gate_proj`
- `model.layers.7.mlp.up_proj`
- `model.layers.7.mlp.down_proj`
- `model.layers.8.self_attn.q_proj`
- `model.layers.8.self_attn.k_proj`
- `model.layers.8.self_attn.v_proj`
- `model.layers.8.self_attn.o_proj`
- `model.layers.8.mlp.gate_proj`
- `model.layers.8.mlp.up_proj`
- `model.layers.8.mlp.down_proj`
- `model.layers.9.self_attn.q_proj`
- `model.layers.9.self_attn.k_proj`
- `model.layers.9.self_attn.v_proj`
- `model.layers.9.self_attn.o_proj`
- `model.layers.9.mlp.gate_proj`
- `model.layers.9.mlp.up_proj`
- `model.layers.9.mlp.down_proj`
- `model.layers.10.self_attn.q_proj`
- `model.layers.10.self_attn.k_proj`
- `model.layers.10.self_attn.v_proj`
- `model.layers.10.self_attn.o_proj`
- `model.layers.10.mlp.gate_proj`
- `model.layers.10.mlp.up_proj`
- `model.layers.10.mlp.down_proj`
- `model.layers.11.self_attn.q_proj`
- `model.layers.11.self_attn.k_proj`
- `model.layers.11.self_attn.v_proj`
- `model.layers.11.self_attn.o_proj`
- `model.layers.11.mlp.gate_proj`
- `model.layers.11.mlp.up_proj`
- `model.layers.11.mlp.down_proj`
- `model.layers.12.self_attn.q_proj`
- `model.layers.12.self_attn.k_proj`
- `model.layers.12.self_attn.v_proj`
- `model.layers.12.self_attn.o_proj`
- `model.layers.12.mlp.gate_proj`
- `model.layers.12.mlp.up_proj`
- `model.layers.12.mlp.down_proj`
- `model.layers.13.self_attn.q_proj`
- `model.layers.13.self_attn.k_proj`
- `model.layers.13.self_attn.v_proj`
- `model.layers.13.self_attn.o_proj`
- `model.layers.13.mlp.gate_proj`
- `model.layers.13.mlp.up_proj`
- `model.layers.13.mlp.down_proj`
- `model.layers.14.self_attn.q_proj`
- `model.layers.14.self_attn.k_proj`
- `model.layers.14.self_attn.v_proj`
- `model.layers.14.self_attn.o_proj`
- `model.layers.14.mlp.gate_proj`
- `model.layers.14.mlp.up_proj`
- `model.layers.14.mlp.down_proj`
- `model.layers.15.self_attn.q_proj`
- `model.layers.15.self_attn.k_proj`
- `model.layers.15.self_attn.v_proj`
- `model.layers.15.self_attn.o_proj`
- `model.layers.15.mlp.gate_proj`
- `model.layers.15.mlp.up_proj`
- `model.layers.15.mlp.down_proj`

> These are only candidates. Actual LoRA targets should be selected based on the model architecture.

## 9. Complete Model Configuration

This section contains the configuration fields actually present in the model. Architecture-specific fields are included automatically.

| Configuration | Value |
|---|---|
| `transformers_version` | `5.16.1` |
| `architectures` | `['LlamaForCausalLM']` |
| `output_hidden_states` | `False` |
| `return_dict` | `True` |
| `dtype` | `bfloat16` |
| `chunk_size_feed_forward` | `0` |
| `is_encoder_decoder` | `False` |
| `id2label` | `{0: 'LABEL_0', 1: 'LABEL_1'}` |
| `label2id` | `{'LABEL_0': 0, 'LABEL_1': 1}` |
| `problem_type` | `N/A` |
| `vocab_size` | `128256` |
| `hidden_size` | `2048` |
| `intermediate_size` | `8192` |
| `num_hidden_layers` | `16` |
| `num_attention_heads` | `32` |
| `num_key_value_heads` | `8` |
| `hidden_act` | `silu` |
| `max_position_embeddings` | `131072` |
| `initializer_range` | `0.02` |
| `rms_norm_eps` | `1e-05` |
| `use_cache` | `True` |
| `pad_token_id` | `N/A` |
| `bos_token_id` | `128000` |
| `eos_token_id` | `[128001, 128008, 128009]` |
| `pretraining_tp` | `1` |
| `tie_word_embeddings` | `True` |
| `rope_parameters` | `{'factor': 32.0, 'high_freq_factor': 4.0, 'low_freq_factor': 1.0, 'original_max_position_embeddings': 8192, 'rope_type': 'llama3', 'rope_theta': 500000.0}` |
| `attention_bias` | `False` |
| `attention_dropout` | `0.0` |
| `mlp_bias` | `False` |
| `head_dim` | `64` |
| `_name_or_path` | `meta-llama/Llama-3.2-1B-Instruct` |
| `model_type` | `llama` |
| `output_attentions` | `False` |

## 10. Human-Friendly Explanation


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


## 11. Architecture Summary

✅ Attention dimensions are consistent: `2048 = 32 × 64`

## 12. First Transformer Layer Structure

```text
LlamaDecoderLayer(
  (self_attn): LlamaAttention(
    (q_proj): Linear(in_features=2048, out_features=2048, bias=False)
    (k_proj): Linear(in_features=2048, out_features=512, bias=False)
    (v_proj): Linear(in_features=2048, out_features=512, bias=False)
    (o_proj): Linear(in_features=2048, out_features=2048, bias=False)
  )
  (mlp): LlamaMLP(
    (gate_proj): Linear(in_features=2048, out_features=8192, bias=False)
    (up_proj): Linear(in_features=2048, out_features=8192, bias=False)
    (down_proj): Linear(in_features=8192, out_features=2048, bias=False)
    (act_fn): SiLUActivation()
  )
  (input_layernorm): LlamaRMSNorm((2048,), eps=1e-05)
  (post_attention_layernorm): LlamaRMSNorm((2048,), eps=1e-05)
)
```

---

*Report generated automatically using the Hugging Face model object.*