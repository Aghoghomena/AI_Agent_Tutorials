from pydantic import BaseModel, Field
from openai import pydantic_function_tool

class Add(BaseModel):
   """Test tool for addition."""
   a: int = Field(description="First number to add")
   b: int = Field(description="Second number to add")

   def exec(self):
     """Simple addition function."""
     return self.a + self.b
   
tool = pydantic_function_tool(Add)

print(tool)

tool_lookup = {"add": Add}
args = {"a": 5, "b": 6}
res = tool_lookup["add"](**args).exec()
print(res)