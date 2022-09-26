# fix_transformation_negative
Change the /entry/instrument/detector/transformations/translation/vector value 2 to positive allowing processing with DIALS

Since a 2022 firmware upgrade, the EIGER-9M detector at proxima2a writes master.h5 files where the detector translation is reported in a standard incompatible with DIALS, a conflict between the IUCR and the Nexus standards. 
This script removes the minus sign on the detector distance.
