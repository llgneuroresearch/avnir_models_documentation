# Supported File Formats

Our models are designed to work exclusively with the NIfTI file format. To ensure compatibility, please follow the recommendations below based on your current file format:

## DICOM Files
If your data is in DICOM format, we highly recommend using [dcm2niix](https://github.com/rordenlab/dcm2niix) to convert your files to NIfTI.

## NRRD Files
For NRRD files, we encourage you to use the `avnir_nrrd_to_nifti` utility from the [avnirpy](https://github.com/llgneuroresearch/avnirpy) package to perform the conversion.

By adhering to these guidelines, you can ensure seamless integration with our models.