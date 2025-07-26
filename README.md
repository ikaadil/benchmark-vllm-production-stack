# Benchmark vLLM Production Stack

Step-by-step instructions to run the benchmark for vLLM production stack.

## Quick Start

Follow these steps in order to set up and run the benchmark:

### 1. Get the vLLM Production Stack

First, clone the `vllm-project/production-stack` repository:

```bash
git clone git@github.com:vllm-project/production-stack.git
cd production-stack
```

### 2. Update the Fake OpenAI Server

Replace the existing fake OpenAI server file in `src/tests/perftest/fake-openai-server.py` with the simpler version from this repository:

### 3. Make Scripts Executable

Give the necessary scripts permission to run:

```bash
chmod +x src/vllm_router/perf-test.sh
chmod +x src/tests/perftest/*.sh
```

### 4. Start the Fake OpenAI Server

Run the mock OpenAI server with these settings:
- `4` = number of server instances
- `500` = max tokens

```bash
bash run-multi-server.sh 4 500
```

### 5. Start the vLLM Router

Launch the router on port 8000:

```bash
bash src/vllm_router/perf-test.sh 8000
```

### 6. Run the Benchmark

Finally, execute the benchmark script from this repository to test performance:

```bash
python3 benchmark.py
```

## What This Does

The benchmark will send 10,000 concurrent requests to vLLM router and measure how long it takes to complete all of them. You'll see output like:

before improvement:
```
Required time: 28.93 seconds
```

After improvement:
```
Required time: 6.70 seconds
```
