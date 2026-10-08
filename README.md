SunshineCTF 2019 Challenges
-----

This is the public release of the challenges from [SunshineCTF 2019](https://ctftime.org/event/767).
Unless otherwise specified, all challenges are released under the [MIT license](LICENSE).

### Repo layout

Challenges are organized as `<Category>/<ChallengeName>`. Most challenge folders contain:

| File name        | Description
|------------------|-------------
| `description.md` | The challenge description as it was shown to players.
| `README.md`      | Author notes: build/deploy info and files for players.
| `writeup.md`     | The intended solution (spoilers!).
| `flag.txt`       | The challenge's flag.

Some challenge files were too large to commit. Those are replaced by a small `.txt` file
that links to where the original file was hosted.

### How to build/deploy the server-based challenges

Install the `pwnmake` command by following the instructions located at https://github.com/C0deH4cker/PwnableHarness.

* To compile all binaries: `pwnmake`
* To build and run Docker containers for all server-based challenges: `pwnmake docker-start` (stop them with `pwnmake docker-stop`)
* To publish all build artifacts that should be distributed to players into the `publish` folder: `pwnmake publish`
* To verify each server-based challenge by running its solver against a local container: `pwnmake check` (`pwnmake check-full` also runs the slow solvers)

Each of these can be sped up by adding an argument like `-j8` to run it with 8
parallel workers.

[`ports.md`](ports.md) lists the port (and hostname, for web challenges) each server-based
challenge uses on the archive at https://ctf.hackucf.org.
