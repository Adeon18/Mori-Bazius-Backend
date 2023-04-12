# Baza
Or whatever we'll call this...


## How to launch and configure Cassandra

Go into the `cassandra` directory - **Note: you MUST be inside the `cassandra` directory to continue!**

```sh
./run-and-configure.sh
```

_This will create a cluster and create tables with proper replication inside._

To **stop** the cluster(from the `cassandra` directory):

```sh
./stop.sh
```

## How to write tests

1. Head into the `app/tests` directory.
2. Create a new file `test_YOURNAMEHERE.py`
3. In file import the module you want to test the following way:

```python
import importlib.util
spec = importlib.util.spec_from_file_location("your_name", "RELATIVE PATH TO MODULE FROM THE tests DIRECTORY")
module_name_in_your_code = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module_name_in_your_code)
```

_Example:_

```python
import importlib.util
spec = importlib.util.spec_from_file_location("tested_app", "../src/app.py")
tested_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tested_app)
```

4. Once finished, you can run them locally via `run-tests.sh` or just push to branch to run remotely.

HM: _`run-tests.sh` gives you coverage if all tests are passed._
