def send_prompt(self, prompts, temperature=0.1):
    if not isinstance(prompts, list):
        raise ValueError('prompts must be a list of strings')

    if any(not prompt for prompt in prompts):
        raise ValueError('prompts cannot contain empty strings')

    if temperature < 0 or temperature > 1:
        raise ValueError('temperature must be between 0 and 1')

    try:
        history = self._conversation_history + [self._construct_message(prompt) for prompt in prompts]
        self.conversation = self.model.start_chat(history=history)
        response = self.conversation.send_message(
            generation_config=self._generation_config(temperature)
        )
        response.resolve()
        return f'{"\n".join(prompts)}\n---' * 20 + f'{"text": "{response.text}"}'
    except Exception as e:
        raise ValueError(e.message)