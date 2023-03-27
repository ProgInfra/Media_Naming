# Import standard libraries
from functools import wraps

# Import installed libraries
import asyncio


def typer_async(f):
  '''
  Async Await Wrapper.
  '''
  @wraps(f)
  def wrapper(*args, **kwargs):
    return asyncio.run(f(*args, **kwargs))
  return wrapper
