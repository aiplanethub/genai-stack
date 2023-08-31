#!/usr/bin/env python

"""Tests for `genai_stack` package."""


import unittest

from genai_stack.memory import ConversationBufferMemory

class TestConversationBufferMemory(unittest.TestCase):
    def test_conversation_buffer_memory(self):
        memory = ConversationBufferMemory(config={})

        # Storing few conversation
        memory.add_text(user_text="hello my name is Ali,what’s your name?",model_text="my name is Mona ,nice to meet you ,Al")
        memory.add_text(user_text="nice to meet you,whats your last name",model_text="it’s Mohamed,and you")
        memory.add_text(user_text="it’s Nader",model_text="what are you doing for living?")

        # Chat history
        print(memory.get_chat_history())

        # User query
        print(memory.get_user_text())

         # Model response
        print(memory.get_model_text())