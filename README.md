# reproducible-cl6x
cl6x compiler produce irreproducible object files, that is: two consecutive builds will produce different binary (md5sum of a resulting artifact will be different).
See also https://reproducible-builds.org/

This project tries try to workaround this issue until that is supported by Texas Instruments (who delivers cl6x). There is the light in the tunnel, as per answer in this topic: https://e2e.ti.com/support/tools/ccs/f/81/t/760093

# Contributing
Contributions are welcomed. Create merge requests.
