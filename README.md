## homestuck_ebooks

Markov generated Homestuck tweets.

Not related to Andrew Hussie.

Instance operated by [@ev1l0rd](http://twitter.com/ev1l0rd) can be found at [@ebooks_hs](https://twitter.com/ebooks_hs).

## Usage

Install `requirements.txt` with pip (`pip install --user requirements.txt`).

Run `download.py`, then run `main.py` once. This will generate a config file.

Create a new application. Name and description don't matter. You can leave the callback URL empty. Generate a consumer key/secret and put them along with the access token and the access secret in the config file.

From that point on, create a cronjob to run `main.py` with the frequency you want it to Tweet. To simplify scheduling cronjobs, I highly recommend using [crontab.guru](https://crontab.guru/)

## License

AGPLv3, with the following additional clause effective on `main.py`:

```
    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it;

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version;
```

```
    homestuck_ebooks - Generate Homestuck tweets with markov chains
    Copyright (C) 2018 - Valentijn "ev1l0rd"

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
```