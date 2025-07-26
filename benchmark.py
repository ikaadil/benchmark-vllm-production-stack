import asyncio
import time
import aiohttp

async def send_post(session):
    url = "http://localhost:8000/v1/chat/completions"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "max_tokens": 128,
        "messages": [
            {
                "content": "You are a helpful assistant.",
                "role": "system"
            },
            {
                "content": "Hello, I'm Ifta",
                "role": "user"
            },
            {
                "content": "What is my name? What is the capital of Bangladesh?",
                "role": "user"
            }
        ],
        "model": "fake_model_name",
        "n": 1,
        "stop": ["###"],
        "temperature": 0.7,
        "user": "user-123"
    }

    async with session.post(url, headers=headers, json=payload) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        start_time = time.perf_counter()

        # Create 10000 tasks for concurrent POST requests
        tasks = [send_post(session) for _ in range(10000)]
        responses = await asyncio.gather(*tasks)

        end_time = time.perf_counter()
        print(f"Required time: {end_time - start_time:.2f} seconds")

asyncio.run(main())

