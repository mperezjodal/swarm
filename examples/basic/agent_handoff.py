from swarm import Swarm, Agent

client = Swarm()

english_agent = Agent(
    name="English Agent",
    instructions="You only speak English.",
)

spanish_agent = Agent(
    name="Spanish Agent",
    instructions="You only speak Spanish.",
)


def transfer_to_spanish_agent():
    """Transfer Spanish speaking users immediately."""
    return spanish_agent


english_agent.functions.append(transfer_to_spanish_agent)

messages = [{"role": "user", "content": "Hola. ¿Cómo estás?"}]
response = client.run(agent=english_agent, messages=messages)

print(response.messages[-1]["content"])
