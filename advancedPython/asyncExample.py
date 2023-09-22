import asyncio

# Define an asynchronous function (coroutine)
async def say_hello(name,time):
    await asyncio.sleep(time)  # Simulate a non-blocking operation (1 second delay)
    print(f"Hello, {name}!")

# Define another asynchronous function
async def main():
    tasks = []  # Create a list to hold the coroutines

    # Create multiple coroutine instances and add them to the list
    tasks.append(say_hello("Alice",1))
    tasks.append(say_hello("Bob",1))
    tasks.append(say_hello("Charlie",3))

    # Execute the coroutines concurrently using asyncio.gather
    await asyncio.gather(*tasks)

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())