import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

old_catch = """        if (appState === 'processing') setAppState('consent');
      }
    }
  };"""

new_catch = """        if (appState === 'processing') setAppState('consent');
      } finally {
        // Clear the input so the user can upload the exact same file again without the browser ignoring it!
        e.target.value = '';
      }
    }
  };"""

if "e.target.value = '';" not in content:
    content = content.replace(old_catch, new_catch)
    file_path.write_text(content, encoding="utf-8")
    print("Fixed React file input bug.")
else:
    print("Already fixed.")
