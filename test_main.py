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
  loop = asyncio.get_event_loop()
  task = loop.create_task(add(123, 456))
  loop.run_until_complete(task)
  assert task.result() == {"summation": 579}

def test_minus():
  task1 = loop.create_task(minus(456, 123))
  loop.run_until_complete(task1)
  assert task1.result() == {"subtraction": 333}

def test_multi():
  task2 = loop.create_task(multi(4, 4))
  loop.run_until_complete(task2)
  assert task2.result() == {"multiplication": 16}

def test_div():
  task3 = loop.create_task(div(24, 4))
  loop.run_until_complete(task3)
  assert task3.result() == {"division": 6}

def test_power():
  task4 = loop.create_task(power(2, 3))
  loop.run_until_complete(task4)
  assert task4.result() == {"power": 8}

def test_sqrt():
  task5 = loop.create_task(sqrt(36))
  loop.run_until_complete(task5)
  assert task5.result() == {"square root": 6}

def test_mod():
  loop = asyncio.get_event_loop()
  task6 = loop.create_task(mod(12, 6))
  loop.run_until_complete(task6)
  assert task6.result() == {"modulo": 0}

def test_fac():
  loop = asyncio.get_event_loop()
  task7 = loop.create_task(fac(12))
  loop.run_until_complete(task7)
  assert task7.result() == {"factorization": '2 2 3'}
