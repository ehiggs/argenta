# Introduction

Tools for dealing with Argenta data. e.g. reformat their csv files, stitch the
files together, and replace some weird counterparty names with the actual names.

If you don't use Argenta, a bank based in Belgium, then this repository is
likely to be of little interest.

# Use

Go to your Argenta account and download the csv files for your account. These
are formatted poorly. They use semicolon (`;`) to delimit the fields. They don't
use utf8 for encoding. The dates are all backwards. And for some reason, they
only allow you to download ~40 rows worth of data at a time.

## `format-csv`
`format-csv` command will slurp up the files, stitch them together,
reorder the lines, and print them out again using comma (`,`) as the delimiter.

```bash
format-csv 'BE123456 (1).csv' 'BE123456 (2).csv' > MyArgentaData.csv
```
## `analyse`

```bash
analyse MyArgentaData.csv
Annual:
Mean income: 123.10
Median income: 123.10
Mean expense: 123.10
Median expense: 123.10
Monthly:
Mean income: 123.10
Median income: 123.10
Mean expense: 123.10
Median expense: 123.10
Daily:
Mean income: 123.10
Median income: 0.00
Mean expense: 123.10
Median expense: 123.10
Itemised:
Mean income: 123.10
Median income: 0.00
Mean expense: 123.10
Median expense: 123.10
```


# Issues

Locales on OSX seem to be messed up. To use these tools you will have to export
your locale variables to use UK English encoded as UTF8. We use `en_GB.utf-8`
and not `en_US.utf-8` because we don't want filthy `mm/dd/yyyy` dates in our
outputs. Well, the code doesn't actually care, but if it *did* use the locale to
determine the output date format, we should be in the habit of using
`en_GB.utf-8`.

```bash
LANG=en_GB.utf-8
LC_ALL=en_GB.utf-8
```
