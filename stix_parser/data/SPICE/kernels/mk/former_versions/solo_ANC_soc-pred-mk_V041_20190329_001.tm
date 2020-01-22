KPL/MK

Meta-kernel for Solar Orbiter Dataset v041 -- Predicted Default 20190329_001
==========================================================================

   This meta-kernel lists the Solar Orbiter Predicted Default SPICE kernels
   providing information for the full mission based on predicted, test
   and/or measured data.

   The kernels listed in this meta-kernel and the order in which
   they are listed are picked to provide the best data available and
   the most complete coverage for the Solar_Orbiter Predicted Default scenario.


Usage of the Meta-kernel
-------------------------------------------------------------------------

   This file is used by the SPICE system as follows: programs that make use
   of this kernel must "load" the kernel normally during program
   initialization. Loading the kernel associates the data items with
   their names in a data structure called the "kernel pool". The SPICELIB
   routine FURNSH loads a kernel into the pool.

   The kernels listed below can be obtained from the ESA SPICE FTP server:

      ftp://spiftp.esac.esa.int/data/SPICE/SOLAR-ORBITER/kernels/


Implementation Notes
-------------------------------------------------------------------------

   It is recommended that users make a local copy of this file and
   modify the value of the PATH_VALUES keyword to point to the actual
   location of the Solar_Orbiter SPICE data set's ``data'' directory on
   their system. Replacing ``/'' with ``\'' and converting line
   terminators to the format native to the user's system may also be
   required if this meta-kernel is to be used on a non-UNIX workstation.


-------------------

   This file was created on March 29, 2019 by Marc Costa Sitja ESA/ESAC.


   \begindata

     PATH_VALUES       = ( '../..' )

     PATH_SYMBOLS      = ( 'KERNELS' )

     KERNELS_TO_LOAD   = (

                           '$KERNELS/ck/solo_ANC_soc-sc-iboom-ck_20180930-21000101_V01.bc'
                           '$KERNELS/ck/solo_ANC_soc-sc-oboom-ck_20180930-21000101_V01.bc'
                           '$KERNELS/ck/solo_ANC_soc-sc-fof-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-eui-fsi-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-eui-hri-euv-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-eui-hri-lya-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-metis-euv-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-metis-vis-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-metis-m0-tel-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-phi-fdt-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-phi-hrt-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-solohi-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-spice-sw-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-spice-lw-ck_20180930-21000101_V02.bc'
                           '$KERNELS/ck/solo_ANC_soc-stix-ck_20180930-21000101_V02.bc'
                           '$KERNELS/../former_versions/misc'
                           'solo_ANC_soc-default-att_20180929-20290412_V01.bc'
                           '$KERNELS/../former_versions/misc'
                           'solo_ANC_soc-spot-track-att_20220303-20220304_V01.bc'
                           '$KERNELS/../former_versions/misc'
                           'solo_ANC_soc-pred-roll-att_20190214-20290611_V01.bc'
                           '$KERNELS/../former_versions/misc'
                           'solo_ANC_soc-pred-roll-att_20250701-20251202_V01.bc'

                           '$KERNELS/fk/solo_ANC_soc-sc-fk_V03.tf'
                           '$KERNELS/fk/solo_ANC_soc-ops-fk_V02.tf'
                           '$KERNELS/fk/solo_ANC_soc-sci-fk_V02.tf'
                           '$KERNELS/fk/earth_topo_050714.tf'
                           '$KERNELS/fk/estrack_v01.tf'
                           '$KERNELS/fk/new_norcia_topo.tf'

                           '$KERNELS/ik/solo_ANC_soc-epd-ik_V02.ti'
                           '$KERNELS/ik/solo_ANC_soc-eui-ik_V01.ti'
                           '$KERNELS/ik/solo_ANC_soc-metis-ik_V02.ti'
                           '$KERNELS/ik/solo_ANC_soc-phi-ik_V01.ti'
                           '$KERNELS/ik/solo_ANC_soc-solohi-ik_V01.ti'
                           '$KERNELS/ik/solo_ANC_soc-spice-ik_V02.ti'
                           '$KERNELS/ik/solo_ANC_soc-stix-ik_V02.ti'
                           '$KERNELS/ik/solo_ANC_soc-swa-ik_V02.ti'

                           '$KERNELS/lsk/naif0012.tls'

                           '$KERNELS/pck/pck00010.tpc'

                           '$KERNELS/sclk/solo_ANC_soc-sclk_20000101_V01.tsc'

                           '$KERNELS/../former_versions/misc'
                           'solo_ANC_soc-orbit_20180930-20290412_V01.bsp'
                           '$KERNELS/spk/de421.bsp'
                           '$KERNELS/spk/estrack_v01.bsp'
                           '$KERNELS/spk/new_norcia.bsp'

                         )

   \begintext


SPICE Kernel Dataset Version
------------------------------------------------------------------------

   The version of this SPICE Kernel Dataset is provided by the following
   keyword:

   \begindata

      SKD_VERSION = 'v041_20190329_001'

   \begintext


Contact Information
------------------------------------------------------------------------

   If you have any questions regarding this file contact SPICE support at
   ESAC:

           Marc Costa Sitja
           (+34) 91-8131-457
           mcosta@sciops.esa.int, esa_spice@sciops.esa.int

End of MK file.