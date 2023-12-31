from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=110)

tree = Tree(":call_me_hand: [link=https://www.extraperks.ai]Vincent Yee", guide_style="bold cyan")
python_tree = tree.add(":computer: Computational Linguist | ML Engineer", guide_style="green")
python_tree.add("⭐ [link=https://github.com/]ML with Audio")
python_tree.add("⭐ [link=https://github.com/]How to ASR")
python_tree.add("⭐ [link=https://github.com/]Performance Prediction")
interests_tree = tree.add(":speaking_head: Interests")
interests_tree.add("Speech Enhancement & Generation")
interests_tree.add("Text Understanding")
interests_tree.add("Python and adjacent communities")
tree.add(":runner: Runner")

about = """\
I’m a Developer passionate about LLM applications focusing on extracting better insights from Text + Audio. 
Been a freelancer, tax analyst and a consultant for the past 5 years. 

I’ve invested significant time in past 3 years volunteering for open source and science organisations like Hugging Face, EuroPython, PyCons across APAC.

I from Singapore!

Follow me on Twitter! [link=https://twitter.com/yyonfai]@yyonfai
"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hey Hey! :wave:", width =60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
