# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WtyczkaQgisProjekt2
                                 A QGIS plugin
 Proste obliczenia
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-09
        copyright            : (C) 2023 by Ada&Rafał
        email                : rafal.chwalek.stud@pw.edu.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WtyczkaQgisProjekt2 class from file WtyczkaQgisProjekt2.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .wtyczka_qgis_projekt_2 import WtyczkaQgisProjekt2
    return WtyczkaQgisProjekt2(iface)