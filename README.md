This repo contains [COVID-19](https://github.com/CSSEGISandData/COVID-19/tree/4a0db2ab780e3e83ff607a0b78810fdcc425f0b6), which is a repo with global case
data of infections with severe acute respiratory syndrome coronavirus 2
(SARS-CoV-2), which was initially named COVID-19. This repository is maintained
by the Center for Systems Science and Engineering at Johns Hopkins University
(JHU CSSE). I am not in any way affiliated with this institution, and can only
gratefully acknowledge the effort undertaken by JHU CSSE. The  directory is
included as a submodule herein, and I plan to periodically fetch updates from
the source. No warranties, of course.

The only problem I had with the data as presented on the COVID-19 website
created by JHU CSSE is that it doesn't make it easy to get a glimpse at the
spread of the disease through time *and* in a particular country/region.

To facilitate this, I created the Python script in the folder [unpivot](./unpivot).
I wanted to have the data in a single csv or Excel file that would include a
view of infections, deaths, recoveries (and, hence, active cases) for each
region/country, and for each date. I wanted this to be in an easy-to-load
format, that can be imported into Excel and digested with a pivot table, with
minimum problems.

The [unpivot](./unpivot) folder will also contain an Excel workbook representing
the output of the last run of my script.