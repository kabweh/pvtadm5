#!/usr/bin/env python
# coding: utf-8
import re
from typing import Dict, Any, List, Optional

class LessonExplainer:
    """
    Generates explanations for educational content in a conversational, teacher-like style.
    """

    def __init__(self):
        """Initialize the lesson explainer."""
        # Placeholder for future model integration or configuration
        pass

    def generate_explanation(self, text: str, complexity_level: str = "medium", source_filename: Optional[str] = None) -> str:
        """
        Generate a conversational, teacher-like explanation for the given text.

        Args:
            text: The text content to explain.
            complexity_level: Desired complexity level (simple, medium, advanced).
            source_filename: The name of the source file (optional, for context).

        Returns:
            Conversational explanation of the content.
        """
        # Remove excessive whitespace and normalize text
        text = self._preprocess_text(text)

        if not text.strip():
            return "I don't see any content to explain. Please upload some material first."

        # Identify the subject matter
        subject = self._identify_subject(text, source_filename)

        # Generate explanation based on complexity level
        # For now, we focus on enhancing the medium level significantly
        if complexity_level == "simple":
            explanation = self._generate_simple_explanation(text, subject)
        elif complexity_level == "advanced":
            explanation = self._generate_advanced_explanation(text, subject)
        else:  # medium (default)
            explanation = self._generate_teacher_explanation(text, subject)

        return explanation

    def _preprocess_text(self, text: str) -> str:
        """
        Preprocess text by removing excessive whitespace and normalizing.

        Args:
            text: Raw text to preprocess.

        Returns:
            Preprocessed text.
        """
        # Replace multiple newlines with a single newline
        text = re.sub(r'\n{3,}', '\n\n', text)
        # Replace multiple spaces with a single space
        text = re.sub(r' {2,}', ' ', text)
        # Attempt to fix common OCR issues like ligatures or misinterpretations
        text = text.replace('ﬁ', 'fi').replace('ﬂ', 'fl')
        # Remove page numbers or headers/footers if possible (simple example)
        text = re.sub(r'^\s*Page \d+\s*$', '', text, flags=re.MULTILINE)
        text = re.sub(r'^\s*Chapter \d+\s*$', '', text, flags=re.MULTILINE)

        return text.strip()

    def _identify_subject(self, text: str, source_filename: Optional[str] = None) -> str:
        """
        Attempt to identify the subject matter of the text, using filename as a hint.

        Args:
            text: The text content to analyze.
            source_filename: The name of the source file (optional).

        Returns:
            Identified subject or "general" if unclear.
        """
        text_lower = text.lower()
        filename_lower = source_filename.lower() if source_filename else ""

        # Prioritize filename hints
        if "ratio" in filename_lower or "math" in filename_lower or "algebra" in filename_lower or "geometry" in filename_lower:
            return "mathematics"
        if "history" in filename_lower:
            return "history"
        if "science" in filename_lower or "biology" in filename_lower or "chemistry" in filename_lower or "physics" in filename_lower:
            return "science"
        if "literature" in filename_lower or "novel" in filename_lower or "poem" in filename_lower:
            return "literature"
        if "language" in filename_lower or "grammar" in filename_lower or "vocabulary" in filename_lower:
            return "language"

        # Fallback to text content analysis
        if any(term in text_lower for term in ['ratio', 'equation', 'formula', 'calculation', 'algebra', 'geometry', 'solve for x', 'fraction', 'decimal', 'percent']):
            return "mathematics"
        if any(term in text_lower for term in ['history', 'century', 'war', 'civilization', 'ancient', 'revolution', 'president', 'king', 'queen']):
            return "history"
        if any(term in text_lower for term in ['science', 'biology', 'chemistry', 'physics', 'experiment', 'molecule', 'atom', 'cell', 'energy', 'force']):
            return "science"
        if any(term in text_lower for term in ['literature', 'novel', 'poem', 'author', 'character', 'story', 'theme', 'metaphor', 'symbolism']):
            return "literature"
        if any(term in text_lower for term in ['grammar', 'vocabulary', 'language', 'verb', 'noun', 'adjective', 'sentence', 'paragraph']):
            return "language"

        return "general"

    def _generate_teacher_explanation(self, text: str, subject: str) -> str:
        """
        Generate a detailed, teacher-like explanation with examples.

        Args:
            text: The text content to explain.
            subject: Identified subject matter.

        Returns:
            Teacher-like explanation.
        """
        # --- This is a placeholder for a more sophisticated LLM call --- #
        # In a real scenario, you'd send the text and subject to an LLM
        # with a prompt designed to elicit a teacher-like explanation.
        # Example Prompt:
        # "You are an expert teacher explaining educational material. 
        #  The subject is {subject}. Explain the following text clearly and 
        #  engagingly for a student. Break down complex ideas, provide 
        #  real-world examples or analogies, and maintain a supportive tone. 
        #  Here is the text: {text}"
        #
        # Since we don't have a live LLM call here, we'll simulate based on subject.

        intro = f"Alright, let's dive into this material on {subject}! I'll break it down for you step-by-step, just like we would in class. Don't worry if it seems tricky at first, we'll figure it out together.\n\n"
        body = ""
        examples = ""
        summary = ""
        outro = "\n\nSo, that's the main idea! How does that sound? Remember, practice makes perfect. If any part is still unclear, please ask! I'm here to help you understand."

        # Simulate explanation based on subject (using the Ratios example)
        if subject == "mathematics":
            if "ratio" in text.lower():
                body = ("First, what *is* a ratio? Think of it like a comparison between two quantities. It tells us how much of one thing there is compared to another. The text mentions you can write ratios in three ways: using the word 'to' (like 3 to 4), using a colon (like 3:4), or as a fraction (like 3/4). They all mean the same thing!\n\n" 
                        "The material also talks about finding ratios in different situations, like comparing red marbles to blue marbles, or cats to dogs. The key is to identify the two quantities you're comparing and write their numbers in the correct order based on the question.\n\n" 
                        "Sometimes, like with fractions, you might need to simplify a ratio. For example, if you have a ratio of 6:8, you can divide both numbers by 2 to get the simpler ratio 3:4. It represents the same relationship, just with smaller numbers.")
                examples = ("\n\n**Let's look at an example:** Imagine you have a fruit bowl with 5 apples and 10 oranges. \n" 
                            "- The ratio of apples to oranges is 5 to 10, or 5:10, or 5/10. \n" 
                            "- We can simplify this! Both 5 and 10 are divisible by 5. So, the simplified ratio is 1:2. This means for every 1 apple, there are 2 oranges.\n" 
                            "- What about the ratio of oranges to *total* fruit? There are 10 oranges and 15 total fruits (5 apples + 10 oranges). So the ratio is 10:15. Can we simplify this? Yes! Both are divisible by 5, giving us 2:3. For every 3 pieces of fruit, 2 are oranges.")
                summary = "\n\n**Key Takeaways:**\n1. A ratio compares two quantities.\n2. You can write ratios using 'to', a colon (:), or as a fraction.\n3. The order matters! Make sure you match the order asked in the question.\n4. Ratios can often be simplified like fractions by dividing both parts by a common factor."
            else:
                # Generic math explanation
                body = "This math topic seems to cover [mention key concepts if identifiable, e.g., solving equations, geometric shapes]. Let's break down the main steps or ideas presented here..."
                examples = "\n\nFor instance, if we're solving an equation like 2x + 3 = 11, the goal is to find the value of 'x'. We'd typically isolate 'x' by performing inverse operations..."
                summary = "\n\nRemember the key steps: [Summarize steps/concepts]."

        elif subject == "history":
            body = "History is like being a detective looking into the past! This text focuses on [mention period/event if identifiable]. It seems to be explaining the causes, key figures, or consequences of this time..."
            examples = "\n\nThink about it like this: If we're studying the American Revolution, we'd look at the causes (like taxes), the key people (like George Washington), and the results (like the creation of the USA)..."
            summary = "\n\nMain points to remember are: [Summarize key events/causes/effects]."

        elif subject == "science":
            body = "Science helps us understand the world around us! This section appears to be about [mention topic if identifiable, e.g., the water cycle, electricity, plant cells]. Let's explore the main processes or concepts..."
            examples = "\n\nFor example, if we're learning about photosynthesis, plants use sunlight, water, and carbon dioxide to make their own food (sugar) and release oxygen. It's like they're tiny food factories!"
            summary = "\n\nKey ideas here are: [Summarize concepts/processes]."

        else: # General subject
            body = "Let's take a closer look at this text. It seems to be discussing [try to infer topic]. The main points are..."
            examples = "\n\nWe can relate this to everyday life. For example..."
            summary = "\n\nIn short, the text explains: [Summarize]."

        # Combine parts
        explanation = intro + body + examples + summary + outro
        return explanation

    # Keep the simple and advanced placeholders, but focus was on medium/teacher
    def _generate_simple_explanation(self, text: str, subject: str) -> str:
        """
        Generate a simple explanation suitable for younger students.
        (Placeholder - less detailed than teacher explanation)
        """
        explanation = f"Hi there! Let's look at this {subject} topic. It's basically saying that... [Simplified summary of the first few sentences]. For example, think about... [Simple analogy]. Does that help a bit?"
        return explanation

    def _generate_advanced_explanation(self, text: str, subject: str) -> str:
        """
        Generate an advanced explanation for older or advanced students.
        (Placeholder - more formal than teacher explanation)
        """
        explanation = f"Analyzing this text on {subject}, we can discern several key principles. Firstly, the concept of [Key Concept 1] is introduced, defined as... This relates to [Key Concept 2] in that... Furthermore, the implications include... A critical perspective might consider... In essence, the material argues that... Would you like a deeper dive into any specific aspect?"
        return explanation

