from pydantic import BaseModel

class A(BaseModel):
    x: str
    y: int = 3

print(A.__fields__)
print(A.parse_obj({'x':'hi','y':2}))
