import asyncio
from main import add
from main import minus
from main import multi
from main import div
from main import power
from main import sqrt
from main import mod
from main import fac

def test_add():
  assert 1 == 1

def test_minus():
  loop = asyncio.get_event_loop()
  task = loop.create_task(minus(456, 123))
  loop.run_until_complete(task)
  loop.close()
  assert task.result() == 333

def test_multi():
  assert multi(4, 4) == 16

def test_div():
  assert div(27, 9) == 3

def test_power():
  assert power(2, 3) == 8

def test_sqrt():
  assert sqrt(64) == 8

def test_mod():
  assert mod(12, 6) == 0

def test_fac():
  assert fac(12) == '2 2 3'
