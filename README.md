# GDAL Test

This project serves to test whether GDAL is correctly installed on a system.

## Preparatory Step
``` 1. pip uninstall gdal ```

``` 2. pip install numpy ```

``` 3. pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"```

NB: it is OK if the step 1 fails, bacause there's no GDAL installed yet.

## Test run
```python main.py```

### Expected output
The succesful program run is expected to produce the following text output:
```
Read 1724 * 1293 data array
Wrote 1724 * 1293 data array

Read 52 features.
```

