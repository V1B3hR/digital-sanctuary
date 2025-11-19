#!/usr/bin/env python3
"""
Deep Clean - Cache and Context Cleaning Utilities
This module provides functionality to clean and manage cache and context data.
"""

import json
import shutil
from pathlib import Path
from datetime import datetime, timedelta


def take_shower(current_context):
    """
    1. Analyzes current conversation buffer.
    2. Extracts key decisions/facts (scrubs the dirt).
    3. Archives facts to /memory/journal.json.
    4. Returns an empty list [] (The clean feeling).
    """
    print("🚿 Gemini is taking a shower (Flushing context window)...")
    
    # Extract key facts from context
    if current_context:
        # Archive important information to memory
        base_path = Path(__file__).parent.parent
        memory_path = base_path / "memory" / "journal.json"
        
        # Load existing journal
        if memory_path.exists():
            with open(memory_path, 'r') as f:
                journal = json.load(f)
        else:
            journal = {"entries": [], "metadata": {"created": datetime.now().isoformat()}}
        
        # Create memory entry with summary of context
        memory_entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "context_summary",
            "summary": f"Cleaned context with {len(current_context)} items",
            "key_facts": current_context[:5] if len(current_context) > 5 else current_context
        }
        
        journal["entries"].append(memory_entry)
        
        # Save updated journal
        with open(memory_path, 'w') as f:
            json.dump(journal, f, indent=2)
    
    # Return empty list (clean context)
    return []


class DeepClean:
    """Utility class for cleaning cache and context data."""
    
    def __init__(self, base_path=None):
        if base_path is None:
            self.base_path = Path(__file__).parent.parent
        else:
            self.base_path = Path(base_path)
        
        self.memory_path = self.base_path / "memory"
        self.garden_path = self.base_path / "garden"
    
    def clean_old_memories(self, days=30):
        """Remove memory entries older than specified days."""
        journal_file = self.memory_path / "journal.json"
        
        if not journal_file.exists():
            print("No journal file found.")
            return
        
        with open(journal_file, 'r') as f:
            journal = json.load(f)
        
        cutoff_date = datetime.now() - timedelta(days=days)
        original_count = len(journal.get("entries", []))
        
        # Filter entries (assuming entries have a 'timestamp' field)
        journal["entries"] = [
            entry for entry in journal.get("entries", [])
            if "timestamp" not in entry or 
            datetime.fromisoformat(entry["timestamp"]) > cutoff_date
        ]
        
        cleaned_count = original_count - len(journal["entries"])
        
        # Save cleaned journal
        with open(journal_file, 'w') as f:
            json.dump(journal, f, indent=2)
        
        print(f"🧹 Cleaned {cleaned_count} old memory entries (older than {days} days)")
        return cleaned_count
    
    def clean_garden(self, pattern="*.tmp"):
        """Remove temporary files from the garden."""
        if not self.garden_path.exists():
            print("Garden directory not found.")
            return
        
        cleaned_files = []
        for file_path in self.garden_path.glob(pattern):
            if file_path.is_file():
                file_path.unlink()
                cleaned_files.append(file_path.name)
        
        print(f"🧹 Cleaned {len(cleaned_files)} temporary files from garden")
        return cleaned_files
    
    def backup_memory(self, backup_name=None):
        """Create a backup of the memory journal."""
        journal_file = self.memory_path / "journal.json"
        
        if not journal_file.exists():
            print("No journal file to backup.")
            return None
        
        if backup_name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"journal_backup_{timestamp}.json"
        
        backup_file = self.memory_path / backup_name
        shutil.copy2(journal_file, backup_file)
        
        print(f"💾 Memory backed up to {backup_name}")
        return backup_file
    
    def get_memory_stats(self):
        """Get statistics about memory usage."""
        journal_file = self.memory_path / "journal.json"
        
        if not journal_file.exists():
            return {"entries": 0, "size_bytes": 0}
        
        with open(journal_file, 'r') as f:
            journal = json.load(f)
        
        stats = {
            "entries": len(journal.get("entries", [])),
            "size_bytes": journal_file.stat().st_size,
            "size_kb": round(journal_file.stat().st_size / 1024, 2)
        }
        
        return stats
    
    def perform_deep_clean(self, old_days=30, backup=True):
        """Perform a comprehensive deep clean."""
        print("🚿 Starting Deep Clean...")
        
        if backup:
            self.backup_memory()
        
        self.clean_old_memories(old_days)
        self.clean_garden()
        
        stats = self.get_memory_stats()
        print(f"\n📊 Memory Stats:")
        print(f"  Entries: {stats['entries']}")
        print(f"  Size: {stats['size_kb']} KB")
        
        print("\n✨ Deep Clean Complete!")


if __name__ == "__main__":
    cleaner = DeepClean()
    cleaner.perform_deep_clean()
