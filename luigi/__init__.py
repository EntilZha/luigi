# -*- coding: utf-8 -*-
#
# Copyright 2012-2015 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
Package containing core luigi functionality.
"""

from luigi import task
from luigi.task import Task, Config, ExternalTask, WrapperTask, namespace

from luigi import target
from luigi.target import Target

from luigi import file  # wtf @ naming
from luigi.file import File, LocalTarget

from luigi import rpc
from luigi.rpc import RemoteScheduler, RPCError
from luigi import parameter
from luigi.parameter import (
    Parameter,
    DateParameter, MonthParameter, YearParameter, DateHourParameter, DateMinuteParameter, DateSecondParameter,
    DateIntervalParameter, TimeDeltaParameter,
    IntParameter, FloatParameter, BooleanParameter, BoolParameter,
    TaskParameter, EnumParameter, DictParameter, ListParameter, TupleParameter
)

from luigi import configuration

from luigi import interface
from luigi.interface import run, build

from luigi import event
from luigi.event import Event

from .tools import range  # just makes the tool classes available from command line


__all__ = [
    'task', 'Task', 'Config', 'ExternalTask', 'WrapperTask', 'namespace',
    'target', 'Target', 'File', 'LocalTarget', 'rpc', 'RemoteScheduler',
    'RPCError', 'parameter', 'Parameter', 'DateParameter', 'MonthParameter',
    'YearParameter', 'DateHourParameter', 'DateMinuteParameter', 'DateSecondParameter', 'range',
    'DateIntervalParameter', 'TimeDeltaParameter', 'IntParameter',
    'FloatParameter', 'BooleanParameter', 'BoolParameter', 'TaskParameter',
    'ListParameter', 'TupleParameter', 'EnumParameter', 'DictParameter',
    'configuration', 'interface', 'file', 'run', 'build', 'event', 'Event'
]
