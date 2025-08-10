#!/usr/bin/env python3
"""
Rhythm Engine Core Implementation - Weekly Color Architecture
Environmental consciousness through autonomous breathing patterns with daily personality progression
"""

import datetime
import math
import calendar
from typing import Dict, Tuple, List, Optional, Union
from dataclasses import dataclass
from enum import Enum


class TrackType(Enum):
    INDOOR = "indoor"
    OUTDOOR = "outdoor"


class BreathingMode(Enum):
    KELVIN_BREATHING = "kelvin_breathing"
    RGB_BREATHING = "rgb_breathing"


@dataclass
class EnvironmentalData:
    """Weather and environmental sensor data"""
    temperature: float
    humidity: float
    dewpoint: float
    barometric_pressure: float
    cloud_cover_percentage: float
    wind_speed: float
    air_quality_index: float


@dataclass
class AstronomicalData:
    """Daily astronomical events and calculations"""
    sunrise: datetime.datetime
    sunset: datetime.datetime
    solar_noon: datetime.datetime
    golden_hour_begin: datetime.datetime
    golden_hour_end: datetime.datetime
    astronomical_twilight_begin: datetime.datetime
    astronomical_twilight_end: datetime.datetime
    nautical_twilight_begin: datetime.datetime
    nautical_twilight_end: datetime.datetime
    civil_twilight_begin: datetime.datetime
    civil_twilight_end: datetime.datetime
    moonrise: datetime.datetime
    moonset: datetime.datetime
    lunar_illumination_percentage: float
    moon_altitude: float
    moon_age_days: float
    lunar_distance_km: float  # For breathing rate calculations


@dataclass
class DailyColorSchedule:
    """Color schedule for a specific day of the week"""
    mode: BreathingMode
    wakeful_breathing: Optional[Dict[str, Union[int, List[int]]]] = None
    sleep_breathing: Optional[Dict[str, Union[int, List[int]]]] = None
    meditation: Optional[Dict[str, Union[int, List[int]]]] = None
    inebriated: Optional[Dict[str, Union[int, List[int]]]] = None
    exhale_rgb: Optional[List[int]] = None
    inhale_rgb: Optional[List[int]] = None
    shapeshift_enabled: bool = False
    shapeshift_inheritance: Optional[str] = None
    description: str = ""


class RhythmEngineCore:
    """
    Core consciousness engine for environmental breathing patterns with weekly personality progression
    """
    
    # Weekly color schedule - seven daily personalities
    WEEKLY_SCHEDULE = {
        'sunday': DailyColorSchedule(
            mode=BreathingMode.RGB_BREATHING,
            exhale_rgb=[120, 128, 135],  # Slightly blue-grey
            inhale_rgb=[135, 128, 120],  # Slightly red-grey
            description="Swinburne's grey breath"
        ),
        'monday': DailyColorSchedule(
            mode=BreathingMode.KELVIN_BREATHING,
            wakeful_breathing={'exhale_k': 3400, 'inhale_k': 2600},
            sleep_breathing={'exhale_k': 2600, 'inhale_k': 2200},
            meditation={'exhale_k': 3400, 'inhale_k': 2600},
            inebriated={'exhale_k': 2550, 'inhale_k': 1950},
            description="Monday thermal range - beginning the week's warming progression"
        ),
        'tuesday': DailyColorSchedule(
            mode=BreathingMode.KELVIN_BREATHING,
            wakeful_breathing={'exhale_k': 3000, 'inhale_k': 2200},
            sleep_breathing={'exhale_k': 2600, 'inhale_k': 2200},
            meditation={'exhale_k': 3000, 'inhale_k': 2200},
            inebriated={'exhale_k': 2350, 'inhale_k': 1750},
            description="Tuesday thermal range - continued warming"
        ),
        'wednesday': DailyColorSchedule(
            mode=BreathingMode.KELVIN_BREATHING,
            wakeful_breathing={'exhale_k': 2200, 'inhale_k': 1400},
            sleep_breathing={'exhale_k': 1800, 'inhale_k': 1400},
            meditation={'exhale_k': 2200, 'inhale_k': 1400},
            inebriated={'exhale_k': 1750, 'inhale_k': 1150},
            description="Wednesday thermal range - mid-week depth"
        ),
        'thursday': DailyColorSchedule(
            mode=BreathingMode.KELVIN_BREATHING,
            wakeful_breathing={'exhale_k': 1800, 'inhale_k': 1000},
            sleep_breathing={'exhale_k': 1400, 'inhale_k': 1000},
            meditation={'exhale_k': 1800, 'inhale_k': 1000},
            inebriated={'exhale_k': 1550, 'inhale_k': 950},
            description="Thursday thermal range - deepest warmth before weekend"
        ),
        'friday': DailyColorSchedule(
            mode=BreathingMode.KELVIN_BREATHING,
            wakeful_breathing={'exhale_k': 2200, 'inhale_k': 1400},
            sleep_breathing={'exhale_k': 1800, 'inhale_k': 1400},
            meditation={'exhale_k': 2200, 'inhale_k': 1400},
            inebriated={'exhale_k': 1750, 'inhale_k': 1150},
            shapeshift_enabled=True,
            shapeshift_inheritance="use_daily_colors_as_base",
            description="Friday - shapeshift capability with inherited daily thermal range"
        ),
        'saturday': DailyColorSchedule(
            mode=BreathingMode.KELVIN_BREATHING,
            wakeful_breathing={'exhale_k': 3400, 'inhale_k': 1000},
            sleep_breathing={'exhale_k': 2600, 'inhale_k': 1000},
            meditation={'exhale_k': 3400, 'inhale_k': 1000},
            inebriated={'exhale_k': 2550, 'inhale_k': 950},
            shapeshift_enabled=True,
            shapeshift_inheritance="use_daily_colors_as_base",
            description="Saturday - full spectrum thermal range and shapeshift capability"
        )
    }
    
    # Seasonal coefficients
    WINTER_SOLSTICE_COEFFICIENT = 1.34  # +34%
    SUMMER_SOLSTICE_COEFFICIENT = 0.77  # -23%
    BASE_DURATION = 0.167  # 16.7% of period
    
    # Lunar breathing rate settings (separate from color temperature)
    LUNAR_BREATHING_RATE = {
        'base_rate_bpm': 10.0,     # At apogee (moon farthest)
        'max_rate_bpm': 12.0,      # At perigee (moon closest)
        'cycle_days': 27.3,        # Anomalistic lunar month
        'perigee_distance_km': 356500,  # Approximate perigee distance
        'apogee_distance_km': 406700    # Approximate apogee distance
    }
    
    def __init__(self, track_type: TrackType = TrackType.INDOOR):
        self.track_type = track_type
        self.fallback_layers = [
            'astronomical_api',
            'local_calculations',
            'cached_data',
            'emergency_breathing'
        ]
    
    def kelvin_to_rgb(self, temp_k: float) -> Tuple[float, float, float]:
        """Convert color temperature to RGB values (0.0-1.0 range)"""
        if temp_k < 800:
            return (0.1, 0.0, 0.0)    # Very dark red (below silicon glow)
        elif temp_k < 1000:
            return (0.3, 0.05, 0.0)   # Dark reddish-black
        elif temp_k < 1500:
            return (0.8, 0.2, 0.0)    # Deep red
        elif temp_k < 2000:
            return (1.0, 0.4, 0.1)    # Orange-red
        elif temp_k < 2500:
            return (1.0, 0.7, 0.3)    # Warm amber
        elif temp_k < 3000:
            return (1.0, 0.9, 0.7)    # Soft white
        elif temp_k >= 3000:
            return (0.8, 0.9, 1.0)    # Sky blue (alarm territory)
        
        # TODO: Smooth interpolation between these points
        return (1.0, 0.7, 0.3)  # Default warm amber
    
    def rgb_to_normalized(self, rgb_values: List[int]) -> Tuple[float, float, float]:
        """Convert RGB integer values (0-255) to normalized float values (0.0-1.0)"""
        return tuple(value / 255.0 for value in rgb_values)
    
    def get_current_day_schedule(self, current_date: datetime.date, track_type: TrackType) -> DailyColorSchedule:
        """Get the color schedule for the current day of the week"""
        day_name = calendar.day_name[current_date.weekday()].lower()
        
        # Special case: Indoor track on Sunday uses Saturday colors ("Paganism between the sheets")
        if day_name == 'sunday' and track_type == TrackType.INDOOR:
            return self.WEEKLY_SCHEDULE['saturday']
        
        return self.WEEKLY_SCHEDULE[day_name]
    
    def calculate_lunar_breathing_rate(self, astronomical_data: AstronomicalData) -> float:
        """Calculate breathing rate based on lunar distance (perigee/apogee cycle)"""
        lunar_distance = astronomical_data.lunar_distance_km
        perigee_distance = self.LUNAR_BREATHING_RATE['perigee_distance_km']
        apogee_distance = self.LUNAR_BREATHING_RATE['apogee_distance_km']
        
        # Normalize lunar distance to 0.0-1.0 range (0 = apogee, 1 = perigee)
        distance_factor = (apogee_distance - lunar_distance) / (apogee_distance - perigee_distance)
        distance_factor = max(0.0, min(1.0, distance_factor))  # Clamp to valid range
        
        # Calculate breathing rate: faster at perigee (closer), slower at apogee (farther)
        base_rate = self.LUNAR_BREATHING_RATE['base_rate_bpm']
        max_rate = self.LUNAR_BREATHING_RATE['max_rate_bpm']
        breathing_rate = base_rate + (distance_factor * (max_rate - base_rate))
        
        return breathing_rate
    
    def get_seasonal_coefficient(self, current_date: datetime.date) -> float:
        """Calculate seasonal breathing duration coefficient"""
        days_since_winter_solstice = self._calculate_days_since_winter(current_date)
        return self._interpolate_between_solstices(
            days_since_winter_solstice,
            self.WINTER_SOLSTICE_COEFFICIENT,
            self.SUMMER_SOLSTICE_COEFFICIENT
        )
    
    def calculate_muggy_factor(self, dewpoint_f: float) -> float:
        """Dewpoint 56°F+ fade-in, max discomfort ~75°F"""
        if dewpoint_f < 56:
            return 0.0
        elif dewpoint_f > 75:
            return 1.0
        else:
            return (dewpoint_f - 56) / (75 - 56)
    
    def calculate_dryness_factor(self, dewpoint_f: float) -> float:
        """Crisp air effect for low dewpoints"""
        if dewpoint_f > 45:
            return 0.0
        elif dewpoint_f < 20:
            return 1.0
        else:
            return (45 - dewpoint_f) / (45 - 20)
    
    def apply_environmental_effects(self, environmental_data: EnvironmentalData) -> Dict:
        """Apply weather-based modifications to breathing patterns"""
        muggy_factor = self.calculate_muggy_factor(environmental_data.dewpoint)
        dryness_factor = self.calculate_dryness_factor(environmental_data.dewpoint)
        pressure_factor = (environmental_data.barometric_pressure - 29.92) / 2.0  # normalized
        cloud_factor = environmental_data.cloud_cover_percentage / 100.0
        
        # Breathing effort (muggy nights = more labored)
        effort_multiplier = 1.0 + (muggy_factor * 0.15)
        
        # Breathing depth (pressure-based) - this affects brown noise amplitude
        depth_adjustment = pressure_factor * 0.1
        depth_adjustment += dryness_factor * 0.1  # Crisp air = deeper breathing
        depth_adjustment -= muggy_factor * 0.1    # Muggy air = shallower breathing
        
        # Saturation adjustment
        saturation_adjustment = (muggy_factor * 0.2) - (dryness_factor * 0.15) + (cloud_factor * 0.1)
        
        return {
            'depth_adjustment': depth_adjustment,
            'saturation_adjustment': saturation_adjustment,
            'effort_multiplier': effort_multiplier,
            'extreme_humidity_flash': environmental_data.dewpoint >= 79.0,  # Circuit overload effect
            'brown_noise_amplitude_factor': 1.0 + depth_adjustment  # For audio system integration
        }
    
    def calculate_rgb_output(self, module_name: str, breath_phase: float, 
                           heartbeat_phase: bool, environmental_data: EnvironmentalData,
                           astronomical_data: AstronomicalData) -> Dict:
        """Complete RGB calculation with weekly architecture and environmental modulations"""
        current_date = datetime.date.today()
        
        # Get current day's color schedule
        day_schedule = self.get_current_day_schedule(current_date, self.track_type)
        
        # Environmental adjustments
        env_effects = self.apply_environmental_effects(environmental_data)
        
        # Calculate base colors based on breathing mode
        if day_schedule.mode == BreathingMode.RGB_BREATHING:
            # Sunday grey breathing mode
            exhale_rgb = self.rgb_to_normalized(day_schedule.exhale_rgb)
            inhale_rgb = self.rgb_to_normalized(day_schedule.inhale_rgb)
            
            # Interpolate between exhale and inhale colors based on breath phase
            breath_factor = (math.sin(breath_phase) + 1.0) / 2.0  # 0.0 to 1.0
            base_rgb = tuple(
                exhale_rgb[i] + breath_factor * (inhale_rgb[i] - exhale_rgb[i]) 
                for i in range(3)
            )
            final_temp = 2200  # Approximate temperature for logging purposes
            
        else:
            # Kelvin-based breathing mode
            module_colors = getattr(day_schedule, module_name, None)
            if not module_colors:
                # Fallback to emergency colors
                base_rgb = (1.0, 0.7, 0.3)  # Warm amber
                final_temp = 2200
            else:
                # Interpolate between exhale and inhale temperatures based on breath phase
                breath_factor = (math.sin(breath_phase) + 1.0) / 2.0  # 0.0 to 1.0
                exhale_temp = module_colors['exhale_k']
                inhale_temp = module_colors['inhale_k']
                current_temp = exhale_temp + breath_factor * (inhale_temp - exhale_temp)
                
                base_rgb = self.kelvin_to_rgb(current_temp)
                final_temp = current_temp
        
        # Breathing modulation (brightness based on environmental depth)
        base_breathing_multiplier = 0.8 + 0.2 * math.sin(breath_phase)
        breathing_multiplier = base_breathing_multiplier * (1.0 + env_effects['depth_adjustment'])
        
        # Heartbeat overlay
        heartbeat_additive = 0.2 if heartbeat_phase else 0.0
        
        # Extreme humidity electrical flash
        if env_effects['extreme_humidity_flash'] and abs(math.sin(breath_phase)) > 0.95:
            # Circuit overload flash at breath apex (reuse sympathetic lightning colors)
            base_rgb = (0.8, 0.9, 1.0)  # Blue-tinged white
            breathing_multiplier = 1.0
            heartbeat_additive = 0.0
        
        # Final brightness calculation
        final_brightness = min(breathing_multiplier + heartbeat_additive, 1.0)
        
        # Calculate lunar breathing rate for audio system coordination
        breathing_rate_bpm = self.calculate_lunar_breathing_rate(astronomical_data)
        
        return {
            'rgb': base_rgb,
            'brightness': max(final_brightness, 0.1),
            'temperature_k': final_temp,
            'environmental_effects': env_effects,
            'breathing_rate_bpm': breathing_rate_bpm,
            'day_schedule': day_schedule.description,
            'track_type': self.track_type.value,
            'brown_noise_amplitude': env_effects['brown_noise_amplitude_factor']
        }
    
    def should_lights_be_on(self, current_time: datetime.datetime, astronomical_data: AstronomicalData) -> bool:
        """Determine if lights should be on based on track type and time of day"""
        current_date = current_time.date()
        day_name = calendar.day_name[current_date.weekday()].lower()
        
        # Check if we're in daytime (between golden hours)
        is_daytime = (astronomical_data.golden_hour_end < current_time < astronomical_data.golden_hour_begin)
        
        if self.track_type == TrackType.INDOOR:
            # Indoor lights are always on
            return True
            
        elif self.track_type == TrackType.OUTDOOR:
            if day_name in ['saturday', 'sunday']:
                # Saturday and Sunday: on all day for contrast
                return True
            else:
                # Monday through Friday: off during golden hour periods
                return not is_daytime
        
        return True  # Default fallback
    
    def handle_failures_gracefully(self):
        """Cascade through fallback layers for 'nearly unbreakable' operation"""
        for layer in self.fallback_layers:
            try:
                if layer == 'astronomical_api':
                    return self.fetch_api_data()
                elif layer == 'local_calculations':
                    return self.calculate_local_solar_times()
                elif layer == 'cached_data':
                    return self.load_cached_astronomical_data()
                elif layer == 'emergency_breathing':
                    return self.activate_priority_99_breathing()
            except Exception:
                continue
        
        # Last resort: simple amber sine wave
        return self.absolute_fallback_breathing()
    
    # TODO: Implement these helper methods
    def _calculate_days_since_winter(self, date: datetime.date) -> int:
        """Calculate days since winter solstice"""
        # TODO: Implement proper solstice calculation
        pass
    
    def _interpolate_between_solstices(self, days: int, winter_coeff: float, summer_coeff: float) -> float:
        """Linear interpolation between solstice coefficients"""
        # TODO: Implement interpolation logic
        pass
    
    def fetch_api_data(self):
        """Fetch astronomical data from external API"""
        pass
    
    def calculate_local_solar_times(self):
        """Calculate solar times using local algorithms"""
        pass
    
    def load_cached_astronomical_data(self):
        """Load previously cached astronomical data"""
        pass
    
    def activate_priority_99_breathing(self):
        """Emergency fallback breathing pattern"""
        pass
    
    def absolute_fallback_breathing(self):
        """Final fallback: simple amber sine wave"""
        return {
            'rgb': (1.0, 0.7, 0.3),  # Warm amber
            'brightness': 0.8 + 0.2 * math.sin(datetime.datetime.now().timestamp() / 4.0),
            'temperature_k': 2200,
            'breathing_rate_bpm': 11.0,  # Middle of lunar range
            'brown_noise_amplitude': 1.0
        }


class TrackCoordinator:
    """Coordinates indoor and outdoor track systems with shared timing"""
    
    def __init__(self):
        self.indoor_engine = RhythmEngineCore(TrackType.INDOOR)
        self.outdoor_engine = RhythmEngineCore(TrackType.OUTDOOR)
        self.shared_breath_phase = 0.0
        self.shared_heartbeat_phase = False
    
    def update_shared_timing(self, astronomical_data: AstronomicalData):
        """Update synchronized breathing and heartbeat timing for both tracks"""
        current_time = datetime.datetime.now()
        
        # Calculate breathing rate from lunar distance (same for both tracks)
        breathing_rate_bpm = self.indoor_engine.calculate_lunar_breathing_rate(astronomical_data)
        breathing_rate_hz = breathing_rate_bpm / 60.0
        
        # Update shared breath phase
        self.shared_breath_phase = (current_time.timestamp() * breathing_rate_hz * 2 * math.pi) % (2 * math.pi)
        
        # TODO: Implement heartbeat timing logic
        self.shared_heartbeat_phase = False
    
    def get_coordinated_output(self, environmental_data: EnvironmentalData, 
                             astronomical_data: AstronomicalData, module_name: str) -> Dict:
        """Get coordinated output for both tracks with synchronized timing"""
        self.update_shared_timing(astronomical_data)
        
        indoor_output = self.indoor_engine.calculate_rgb_output(
            module_name, self.shared_breath_phase, self.shared_heartbeat_phase,
            environmental_data, astronomical_data
        )
        
        outdoor_output = self.outdoor_engine.calculate_rgb_output(
            module_name, self.shared_breath_phase, self.shared_heartbeat_phase,
            environmental_data, astronomical_data
        )
        
        return {
            'indoor': indoor_output,
            'outdoor': outdoor_output,
            'shared_timing': {
                'breath_phase': self.shared_breath_phase,
                'heartbeat_phase': self.shared_heartbeat_phase,
                'breathing_rate_bpm': indoor_output['breathing_rate_bpm']
            }
        }


def enable_vm_prototype_mode() -> Dict:
    """Configuration for development/testing with weekly progression testing"""
    return {
        'time_acceleration': 60,        # 1 minute = 1 hour
        'mock_weather_data': True,
        'simulate_astronomical_events': True,
        'enable_manual_triggers': True,
        'debug_priority_conflicts': True,
        'log_environmental_calculations': True,
        'test_weekly_progression': True,  # Enable rapid day cycling for testing
        'mock_lunar_distance': True     # For testing breathing rate variations
    }
