Port Assignments
-----

Port assignment convention (shared across all SunshineCTF archive years):

    port = yycnn

- `yy` = last 2 digits of the competition year (19 for 2019)
- `c`  = category: 0 pwn, 1 reversing, 2 scripting, 3 web, 4 crypto, 5 misc
- `nn` = challenge index within the category (starting at 01)

Only challenges with a hosted server-side component are listed. Raw TCP
challenges are reached with `nc ctf.hackucf.org <port>`. HTTP(S) web challenges
are served behind nginx on a per-challenge subdomain `<slug>.ctf.hackucf.org`
(the container is bound to `127.0.0.1:<port>` and nginx terminates TLS).

| Challenge Name          | Category  | Author      | Directory                     | Host                                        | Port  | Connection                                        |
|-------------------------|-----------|-------------|-------------------------------|---------------------------------------------|------:|---------------------------------------------------|
| return-to-mania         | Pwn       | bambu       | Pwn/return-to-mania           | ctf.hackucf.org                             | 19001 | `nc ctf.hackucf.org 19001`                        |
| CyberRumble             | Pwn       | kcolley     | Pwn/CyberRumble               | ctf.hackucf.org                             | 19002 | `nc ctf.hackucf.org 19002`                        |
| TimeWarp                | Scripting | Mesaj2000   | Scripting/TimeWarp            | ctf.hackucf.org                             | 19201 | `nc ctf.hackucf.org 19201`                        |
| Entry Exam              | Scripting | dmaria      | Scripting/EntryExam           | entryexam.ctf.hackucf.org              | 19202 | https://entryexam.ctf.hackucf.org            |
| WrestlerBook            | Web       | dmaria      | Web/WrestlerBook              | wrestlerbook.ctf.hackucf.org           | 19301 | https://wrestlerbook.ctf.hackucf.org         |
| Wrestler Name Generator | Web       | dmaria      | Web/WrestlerNameGenerator     | wrestlernamegenerator.ctf.hackucf.org  | 19302 | https://wrestlernamegenerator.ctf.hackucf.org|
| Enter the Polygon       | Web       | pontifex    | Web/EnterthePolygon           | enterthepolygon.ctf.hackucf.org        | 19303 | https://enterthepolygon.ctf.hackucf.org      |
| portfolio               | Web       | dmaria      | Web/portfolio                 | portfolio.ctf.hackucf.org              | 19304 | https://portfolio.ctf.hackucf.org            |
| 16-bit AES              | Crypto    |             | Crypto/16BitAES               | ctf.hackucf.org                             | 19401 | `nc ctf.hackucf.org 19401`                        |
