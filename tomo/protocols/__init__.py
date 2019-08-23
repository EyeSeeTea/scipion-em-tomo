# **************************************************************************
# *
# * Authors:     J.M. De la Rosa Trevin (delarosatrevin@scilifelab.se) [1]
# *
# * [1] SciLifeLab, Stockholm University
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************

import pyworkflow

from .protocol_base import ProtTomoBase, ProtTomoReconstruct, ProtTomoPicking
from .protocol_ts_import import ProtImportTiltSeries
from .protocol_ts_correct_motion import ProtTsCorrectMotion, ProtTsAverage
from .protocol_ts_estimate_ctf import ProtTsEstimateCTF
from .protocol_import_tomograms import ProtImportTomograms
from .protocol_import_subtomograms import ProtImportSubTomograms
from .protocol_import_coordinates import ProtImportCoordinates3D

from .move_to_plugins.protocol_ts_motioncor import ProtTsMotionCorr
from .move_to_plugins.protocol_ts_ctffind import ProtTsCtffind
from .move_to_plugins.protocol_ts_gctf import ProtTsGctf
from .move_to_plugins.protocol_imod_auto3d import ProtImodAuto3D
from .move_to_plugins.protocol_imod_etomo import ProtImodEtomo


protUserSubSet = pyworkflow.em.ProtUserSubSet
setattr(protUserSubSet, "_createSetOfSubTomograms", ProtTomoBase._createSetOfSubTomograms.__func__)
setattr(protUserSubSet, "_createSetOfTomograms", ProtTomoBase._createSetOfTomograms.__func__)
setattr(protUserSubSet, "_createSet", ProtTomoBase._createSet.__func__)

