# crontab

## 3 cron jobs commands
- One should pull down data from an API once a day (don’t care about what time)
  - `0 0 * * * python3 /home/mengyao/crontab/code.py`

- One should pull down data every Sunday night at 10:00pm
  - `0 22 * * SUN ython3 /home/mengyao_hu/crontab/code.py`

- One pull down data at the end of every quarter
  - `0 0 30 */3 * python3 /home/mengyao_hu/crontab/code.py`

## Python file
- data is saved as .txt file and saved locally on the same vm where the cron jobs are running
- screenshots are saved in the "scerenshot" folder
