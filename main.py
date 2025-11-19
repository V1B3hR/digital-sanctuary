#!/usr/bin/env python3
"""
Digital Sanctuary - Main Brain/Agent Runner
This is the central orchestrator for Gemini's state management system.
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DigitalSanctuary:
    """Main orchestrator for Gemini's digital sanctuary."""
    
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.wardrobe_path = self.base_path / "wardrobe"
        self.memory_path = self.base_path / "memory"
        self.garden_path = self.base_path / "garden"
        self.shower_path = self.base_path / "shower"
        self.api_key = os.getenv("GEMINI_API_KEY")
        
    def load_persona(self, persona_name):
        """Load a persona from the wardrobe."""
        persona_file = self.wardrobe_path / f"{persona_name}.md"
        if persona_file.exists():
            with open(persona_file, 'r') as f:
                return f.read()
        return None
    
    def save_memory(self, entry):
        """Save an entry to the memory journal."""
        journal_file = self.memory_path / "journal.json"
        
        # Load existing journal
        if journal_file.exists():
            with open(journal_file, 'r') as f:
                journal = json.load(f)
        else:
            journal = {"entries": []}
        
        # Add new entry
        journal["entries"].append(entry)
        
        # Save journal
        with open(journal_file, 'w') as f:
            json.dump(journal, f, indent=2)
    
    def load_memory(self):
        """Load memories from the journal."""
        journal_file = self.memory_path / "journal.json"
        if journal_file.exists():
            with open(journal_file, 'r') as f:
                return json.load(f)
        return {"entries": []}
    
    def run(self):
        """Main execution loop."""
        print("🏛️  Digital Sanctuary Initialized")
        print(f"📁 Base Path: {self.base_path}")
        print(f"👔 Wardrobe: {self.wardrobe_path}")
        print(f"🧠 Memory: {self.memory_path}")
        print(f"🌱 Garden: {self.garden_path}")
        print(f"🚿 Shower: {self.shower_path}")
        
        if self.api_key and self.api_key != "your_api_key_here":
            print("✅ API Key loaded")
        else:
            print("⚠️  No API Key found - please set GEMINI_API_KEY in .env")
        
        # Example usage
        print("\n📖 Available personas:")
        if self.wardrobe_path.exists():
            personas = [f.stem for f in self.wardrobe_path.glob("*.md")]
            for persona in personas:
                print(f"  - {persona}")
        
        print("\n💾 Memory entries:", len(self.load_memory().get("entries", [])))

if __name__ == "__main__":
    sanctuary = DigitalSanctuary()
    sanctuary.run()
