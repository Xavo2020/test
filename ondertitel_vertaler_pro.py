import sys
import os
import re
import json
import requests
import subprocess
import threading
import webbrowser
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog, font
import pysubs2
import language_tool_python
from langdetect import detect_langs
import appdirs
import hashlib

try:
    from spellchecker import SpellChecker
except ImportError:
    SpellChecker = None

ADMIN_PASSWORD_HASH = "54e00c529be462a708f194e05ce647d1905c75f9c034d0953dcc085abb7d9da9"


def hash_password(password: str) -> str:
    """Hash een wachtwoord met SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def check_admin_password(input_password: str) -> bool:
    """Controleer of een ingevoerd wachtwoord overeenkomt met de ADMIN_PASSWORD_HASH."""
    if not input_password:
        return False
    hashed_input = hash_password(input_password.strip())
    return hashed_input == ADMIN_PASSWORD_HASH



# ---------------------- ESCAPE TRIPLE QUOTES HULPFUNCTIE ----------------
GITHUB_SCRIPT_URL = "https://raw.githubusercontent.com/Xavo2020/https://raw.githubusercontenhttps://raw.githubusercontent.com/Xavo2020/python-ondertitel_vertaler_pro/refs/heads/main/ondertitel_verthttps://raw.githubusercontent.com/Xavo2020/python-ondertitel_vertaler_pro/refs/heads/main/ondertitel_vertaler_pro.py?token=GHSAT0AAAAAADMC57KFO4453CIOQAVKFJBG2G2NADAaler_pro.py?token=GHSAT0AAAAAADMC57KFO4453CIOQAVKFJBG2G2NADAt.com/Xavo2020/Ondertitel_vertaler_pro-2025/refs/heads/main/ondertitel_vertaler_pro.py?token=GHSAT0AAAAAADMC57KEKQ5VJW44PTVZZKXW2G2MIQQOndertitel_vertaler_pro-2025/refs/heads/main/ondertitel_vertaler_pro.py?token=GHSAT0AAAAAADMC57KEKQ5VJW44PTVZZKXW2G2MIQQ"
    


def escape_triple_quotes(content: str) -> str:
    """
    Vervang alle voorkomens van triple-quotes (drie enkele of drie dubbele aanhalingstekens) met een escaped versie
    om te voorkomen dat de Python-string te vroeg wordt afgesloten.
    """
    content = content.replace('"""', '\\"""')
    content = content.replace("'''", "\\'''")
    return content

# ---------------------- BEGIN EXTRA NEO THEMES ----------------------


def extra_neo_themes():
    return {
        'neo_dark_cyan_pink': {
            'bg': '#0A1A1A',
            'fg': '#FF69B4',
            'accent': '#00FFFF',
            'tab': '#1A2A2A',
            'entry_bg': '#112233',
            'entry_fg': '#FF69B4',
            'button_fg': '#000000',
            'button_bg': '#00FFFF',
            'button_active': '#FF69B4',
            'red': '#FF0080',
            'blue': '#00FFFF',
            'green': '#00FF99',
            'border': '#FF69B4'
        },
        'neo_dark_orange_blue': {
            'bg': '#1A0A00',
            'fg': '#FFA500',
            'accent': '#00BFFF',
            'tab': '#2A1A10',
            'entry_bg': '#332211',
            'entry_fg': '#FFA500',
            'button_fg': '#FFFFFF',
            'button_bg': '#00BFFF',
            'button_active': '#FFA500',
            'red': '#FF4500',
            'blue': '#00BFFF',
            'green': '#ADFF2F',
            'border': '#FFA500'
        },
        'neo_dark_purple_green': {
            'bg': '#1A0033',
            'fg': '#00FF99',
            'accent': '#A020F0',
            'tab': '#2A0055',
            'entry_bg': '#290073',
            'entry_fg': '#00FF99',
            'button_fg': '#FFFFFF',
            'button_bg': '#A020F0',
            'button_active': '#00FF99',
            'red': '#FF00FF',
            'blue': '#00FFFF',
            'green': '#00FF99',
            'border': '#A020F0'
        },
        'neo_dark_gold_teal': {
            'bg': '#222211',
            'fg': '#FFD700',
            'accent': '#20B2AA',
            'tab': '#333322',
            'entry_bg': '#444433',
            'entry_fg': '#FFD700',
            'button_fg': '#000000',
            'button_bg': '#20B2AA',
            'button_active': '#FFD700',
            'red': '#FF6347',
            'blue': '#20B2AA',
            'green': '#FFD700',
            'border': '#FFD700'
        },
        'neo_dark_white_black': {
            'bg': '#111111',
            'fg': '#FFFFFF',
            'accent': '#CCCCCC',
            'tab': '#222222',
            'entry_bg': '#222222',
            'entry_fg': '#FFFFFF',
            'button_fg': '#000000',
            'button_bg': '#FFFFFF',
            'button_active': '#CCCCCC',
            'red': '#FF0080',
            'blue': '#00FFFF',
            'green': '#00FF00',
            'border': '#FFFFFF'
        },
        'neo_dark_rainbow': {
            'bg': '#1A1A1A',
            'fg': '#FF69B4',
            'accent': '#00FFFF',
            'tab': '#222222',
            'entry_bg': '#111111',
            'entry_fg': '#FFD700',
            'button_fg': '#FFFFFF',
            'button_bg': '#FF69B4',
            'button_active': '#00FF00',
            'red': '#FF0080',
            'blue': '#00FFFF',
            'green': '#00FF00',
            'border': '#FFD700'
        },
        'neo_dark_white_black': {
            'bg': '#111111',
            'fg': '#FFFFFF',
            'accent': '#CCCCCC',
            'tab': '#222222',
            'entry_bg': '#222222',
            'entry_fg': '#FFFFFF',
            'button_fg': '#000000',
            'button_bg': '#FFFFFF',
            'button_active': '#CCCCCC',
            'red': '#FF0080',
            'blue': '#00FFFF',
            'green': '#00FF00',
            'border': '#FFFFFF'
        },
        'neo_dark_rainbow': {
            'bg': '#1A1A1A',
            'fg': '#FF69B4',
            'accent': '#00FFFF',
            'tab': '#222222',
            'entry_bg': '#111111',
            'entry_fg': '#FFD700',
            'button_fg': '#FFFFFF',
            'button_bg': '#FF69B4',
            'button_active': '#00FF00',
            'red': '#FF0080',
            'blue': '#00FFFF',
            'green': '#00FF00',
            'border': '#FFD700'
        }
    }

# ---------------------- RESOURCE PATH ----------------------


def resource_path(relative_path):
    """
    Voor PyInstaller (als je dit wilt bundelen) of anders, gebruik dit om
    resources mee te nemen in de bundel.
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)


# ---------------------- APPLICATIEPADEN & SETTINGS ----------------------
APPNAME = 'SubtitleTranslatorPRO'
APPAUTHOR = 'MyCompany'
appdata_dir = appdirs.user_data_dir(APPNAME, APPAUTHOR, roaming=True)
os.makedirs(appdata_dir, exist_ok=True)
CONFIG_DIR = os.path.join(appdata_dir, 'config')
os.makedirs(CONFIG_DIR, exist_ok=True)
MODELS_DIR_DEFAULT = os.path.join(appdata_dir, 'models')
os.makedirs(MODELS_DIR_DEFAULT, exist_ok=True)
SCRIPT_EXPORT_DIR_DEFAULT = os.path.join(appdata_dir, 'script_export')
os.makedirs(SCRIPT_EXPORT_DIR_DEFAULT, exist_ok=True)
ERROR_LOG_FILE = os.path.join(appdata_dir, 'error.log')
LIST_CONVERTER_EXPORT_DIR = os.path.join(appdata_dir, 'list_converter_export')
os.makedirs(LIST_CONVERTER_EXPORT_DIR, exist_ok=True)
EXTERNAL_MODEL_DIR_FILE = os.path.join(appdata_dir, 'external_model_dir.txt')


def log_error(msg, settings_dict):
    try:
        if not os.path.exists(settings_dict.get('error_log', ERROR_LOG_FILE)):
            with open(settings_dict.get('error_log', ERROR_LOG_FILE), 'w', encoding='utf-8'):
                pass
        with open(settings_dict.get('error_log', ERROR_LOG_FILE), 'a', encoding='utf-8') as f:
            f.write(msg + '\n')
    except BaseException:
        pass


def clear_error_log(settings_dict):
    try:
        if os.path.exists(settings_dict.get('error_log', ERROR_LOG_FILE)):
            with open(settings_dict.get('error_log', ERROR_LOG_FILE), 'w', encoding='utf-8'):
                pass
    except BaseException:
        pass


DEFAULT_SETTINGS = {
    'theme': 'neo_dark',
    'font_family': 'Segoe UI',
    'font_size': 12,
    'text_style': 'normaal',
    'timeout': 30,
    'target_language': 'Nederlands',
    'servers': {
        'ollama': {
            'key': '',
            'url': 'http://127.0.0.1',
            'port': 11434,
            'active': True,
            'timeout': 30,
            'gpu_support': {
                'enabled': True,
                'num_gpu_layers': 100,
                'gpu_memory': 'auto',
                'gpu_batch_size': 512
            }
        },
        'deepl': {
            'key': '',
            'active': True,
            'timeout': 30
        },
        'hugo': {
            'url': 'http://127.0.0.1',
            'port': 5678,
            'active': True,
            'timeout': 30
        }
    },
    'models': [
        'llama3:8b',
        'mistral:8x7b',
        'llama2:7b'
    ],
    'active_model': 'llama3:8b',
    'external_model_dir': '',
    'error_log': ERROR_LOG_FILE,
    'spelling_language': 'Automatisch',
    'models_dir': MODELS_DIR_DEFAULT,
    'script_export_dir': SCRIPT_EXPORT_DIR_DEFAULT,
    'script_download_if_exe': True
}
SETTINGS_FILE = os.path.join(CONFIG_DIR, 'settings.json')


def load_settings():
    """Laadt de gebruikersinstellingen uit JSON. Als ze niet bestaan, maak defaults aan."""
    if not os.path.exists(SETTINGS_FILE):
        s = DEFAULT_SETTINGS.copy()
        with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
            json.dump(s, f, indent=2, ensure_ascii=False)
        return s
    with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
        try:
            s = json.load(f)
        except BaseException:
            s = DEFAULT_SETTINGS.copy()
            with open(SETTINGS_FILE, 'w', encoding='utf-8') as fw:
                json.dump(s, fw, indent=2, ensure_ascii=False)
            return s
    # Zorg dat nieuw toegevoegde keys altijd aanwezig zijn
    for k, v in DEFAULT_SETTINGS.items():
        if k not in s:
            s[k] = v
        elif isinstance(v, dict) and isinstance(s[k], dict):
            for sk, sv in v.items():
                if sk not in s[k]:
                    s[k][sk] = sv
                if isinstance(sv, dict) and isinstance(s[k][sk], dict):
                    for ssk, ssv in sv.items():
                        if ssk not in s[k][sk]:
                            s[k][sk][ssk] = ssv
    return s


def save_settings(settings):
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=2, ensure_ascii=False)


FILTERS_CONFIG_FILE = os.path.join(CONFIG_DIR, 'filters_config.json')
ZINNEN_DICT = {'Do not allow them to sound the alarm.':
               'Laat ze niet toe om het alarm af te laten gaan'}
MILITARY_TERMS_DICT = {
    'AAA': 'Anti-Aircraft Artillery',
    'AAW': 'Anti-Air Warfare',
    'ABM': 'Anti-Ballistic Missile',
    'AFV': 'Armored Fighting Vehicle',
    'AWACS': 'Airborne Warning and Control System'
}
SPECIALE_WOORDEN_DICT = {
    'Fuck': 'fuck',
    'Yes': 'Ja',
    'No': 'Nee',
    'Copy': 'begrepen'
}
USER_CUSTOM_DICT = {
    'Amsterdam': 'Amsterdam',
    'Nederland': 'Nederland',
    'Nederlands': 'Nederlands',
    'Phoenix': 'Phoenix'
}
DEFAULT_FILTER_CONFIG = {
    'filters_enabled': False,
    'lists': [
        {
            'name': 'Zinnen Lijst',
            'enabled': False,
            'file_format': 'json',
            'source_url': '',
            'priority': 1,
            'items': ZINNEN_DICT
        },
        {
            'name': 'Speciale Woorden',
            'enabled': False,
            'file_format': 'json',
            'source_url': '',
            'priority': 2,
            'items': SPECIALE_WOORDEN_DICT
        },
        {
            'name': 'Military Terms',
            'enabled': False,
            'file_format': 'json',
            'source_url': '',
            'priority': 3,
            'items': MILITARY_TERMS_DICT
        },
        {
            'name': 'Eigen Aanpassingen',
            'enabled': False,
            'file_format': 'json',
            'source_url': '',
            'priority': 4,
            'items': USER_CUSTOM_DICT
        }
    ]
}


def load_filters_config():
    if not os.path.exists(FILTERS_CONFIG_FILE):
        with open(FILTERS_CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_FILTER_CONFIG, f, indent=2, ensure_ascii=False)
        return DEFAULT_FILTER_CONFIG
    with open(FILTERS_CONFIG_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except BaseException:
            data = DEFAULT_FILTER_CONFIG.copy()
            with open(FILTERS_CONFIG_FILE, 'w', encoding='utf-8') as fw:
                json.dump(data, fw, indent=2, ensure_ascii=False)
            return data
    for lst in data.get('lists', []):
        if 'priority' not in lst:
            lst['priority'] = 5
    return data


def save_filters_config(config):
    with open(FILTERS_CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def srt_time(ms):
    h, ms = divmod(ms, 3600000)
    m, s = divmod(ms, 60000)
    s, ms = divmod(s, 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'


def fully_clean_subtitle_line(txt):
    txt = re.sub(r'\\[.*?\\]', '', txt)
    txt = re.sub(r'\\(.*?\\)', '', txt)
    txt = re.sub(r'\\{.*?\\}', '', txt)
    txt = re.sub(r'\\<.*?\\>', '', txt)
    txt = re.sub(r'\\s+', ' ', txt).strip()
    return txt


def apply_filter_lists(txt, filter_config):
    # Eventuele filter-implementatie
    return txt


LANG_TOOL_MAP = {
    'Nederlands': 'nl-NL',
    'Engels': 'en-US',
    'Duits': 'de-DE',
    'Frans': 'fr-FR',
    'Spaans': 'es-ES',
    'Italiaans': 'it-IT',
    'Portugees': 'pt-PT',
    'Pools': 'pl-PL',
    'Russisch': 'ru-RU',
    'Japans': 'ja-JP',
    'Chinees': 'zh-CN'
}

LANGUAGE_PROMPT_MAP = {
    'Nederlands': 'Dutch',
    'Engels': 'English',
    'Duits': 'German',
    'Frans': 'French',
    'Spaans': 'Spanish',
    'Italiaans': 'Italian',
    'Portugees': 'Portuguese',
    'Pools': 'Polish',
    'Russisch': 'Russian',
    'Japans': 'Japanese',
    'Chinees': 'Chinese'
}

LANGDETECT_CODE_MAP = {
    'nl': 'Nederlands',
    'en': 'Engels',
    'de': 'Duits',
    'fr': 'Frans',
    'es': 'Spaans',
    'it': 'Italiaans',
    'pt': 'Portugees',
    'pl': 'Pools',
    'ru': 'Russisch',
    'ja': 'Japans',
    'zh': 'Chinees'
}


def map_detected_language_code(detected_code):
    if not detected_code:
        return 'Engels'
    code_lower = detected_code.lower()
    for c in LANGDETECT_CODE_MAP:
        if code_lower.startswith(c):
            return LANGDETECT_CODE_MAP[c]
    return 'Engels'


try:
    import fasttext
    _fasttext_available = True
except ImportError:
    _fasttext_available = False

_fasttext_model = None


def load_fasttext_model():
    global _fasttext_model
    if not _fasttext_model and _fasttext_available:
        FASTTEXT_MODEL_PATH = os.path.join(appdata_dir, 'lid.176.bin')
        if os.path.exists(FASTTEXT_MODEL_PATH):
            _fasttext_model = fasttext.load_model(FASTTEXT_MODEL_PATH)


def detect_language_fasttext(txt):
    if not _fasttext_available:
        return None
    load_fasttext_model()
    if not _fasttext_model:
        return None
    prediction = _fasttext_model.predict(txt.replace('\n', ' '), k=1)
    if prediction and prediction[0]:
        label = prediction[0][0]
        if label.startswith('__label__'):
            return label.replace('__label__', '').strip()
    return None


def detect_language_fallback(txt):
    if not txt.strip():
        return 'en'
    code_ft = detect_language_fasttext(txt)
    if code_ft:
        return code_ft
    try:
        possible_langs = detect_langs(txt)
        if possible_langs:
            best_match = max(possible_langs, key=lambda l: l.prob)
            if best_match.prob < 0.5:
                return 'en'
            return best_match.lang
    except BaseException:
        pass
    return 'en'


def correct_spelling(
        txt,
        target_lang_name,
        tool_settings,
        parent_instance=None):
    tool_lang = LANG_TOOL_MAP.get(target_lang_name, 'en-US')
    try:
        if tool_lang.lower().startswith('en-'):
            if parent_instance and hasattr(parent_instance, 'spellchecker'):
                local_spellchecker = parent_instance.spellchecker
            else:
                local_spellchecker = SpellChecker(
                    distance=1) if SpellChecker else None
            if local_spellchecker is None:
                return txt
            words = txt.split()
            corrected_words = []
            for word in words:
                if not word.isdigit() and word.isalpha() and (word.islower() or word.istitle()):
                    c = local_spellchecker.correction(word)
                    corrected_words.append(c)
                else:
                    corrected_words.append(word)
            return ' '.join(corrected_words)
        else:
            from language_tool_python import utils
            tool = language_tool_python.LanguageToolPublicAPI(tool_lang)
            matches = tool.check(txt)
            return utils.correct(txt, matches)
    except Exception as e:
        log_error(f'Spelling correction error: {e}', tool_settings)
        return txt


def stop_all_model_servers(settings):
    for srv in settings['servers']:
        if settings['servers'][srv]['active']:
            try:
                if sys.platform == 'win32':
                    subprocess.run(f'taskkill /IM "{srv}.exe" /F', shell=True)
                else:
                    subprocess.run(f'pkill -f {srv}', shell=True)
            except Exception as e:
                log_error(f'{srv} stop error: {e}', settings)
    messagebox.showinfo('Noodstop', 'Alle actieve modelservers zijn gestopt.')


def remove_ai_disclaimers(text):
    whitelist = [
        'schendingen inhoudt van de wet',
        'ongepaste handelwijzen',
        'scheldwoord',
        'scheldwoorden',
        'vloeken',
        'grof taalgebruik',
        'porno',
        'pornografie',
        'seks',
        'sex',
        'drugs',
        'drugsgebruik',
        'discriminatie',
        'racisme',
        'haat',
        'haatspraak',
        'geweld',
        'illegale activiteiten',
        'illegale inhoud',
        'explosieven',
        'terrorisme',
        'misbruik',
        'kindermisbruik',
        'pedofilie',
        'zelfmoord',
        'zelfbeschadiging',
        'zelfdoding',
        'moord',
        'verkrachting'
    ]
    lines = text.splitlines()
    keep_lines = []
    for line in lines:
        if any(w.lower() in line.lower() for w in whitelist):
            keep_lines.append(line)
    cleaned = '\n'.join(lines)
    patterns = [
        '(?i)\\bAs (an? )?AI (language )?model.*',
        '(?i)\\bI am (an? )?AI (language )?model.*',
        '(?i)\\bAs ChatGPT.*',
        '(?i)\\bOpenAI is not responsible.*',
        '(?i)\\bI apologize.*',
        '(?i)\\bI cannot provide.*',
        "(?i)\\bI can\\'t provide.*",
        "(?i)\\bI\\'m sorry.*",
        '(?i)\\bNote:\\s?.*',
        '(?i)\\bThis translation aims.*',
        '(?i)\\bPlease provide .*',
        '(?i)\\bHere is the translation.*',
        '(?i)\\bHere.*((T|t)ranslatie|translation).*',
        '(?i)\\bThe translation of.*',
        '(?i)\\bI will now translate.*',
        '(?i)\\bIn summary, the translation.*',
        "(?i)\\bI\\'ve translated.*",
        '(?i)\\bI used The.*',
        '(?i)\\bWhich I.*',
        '(?i)\\bWich I.*',
        '(?i)\\bWould be happy to help.*',
        '(?i)\\bIf you want a more.*',
        '(?i)\\bThis text is meant.*',
        '(?i)\\bLet me know.*',
        '(?i)\\bdisclaimer.*',
        '(?i)\\bPlease refrain from using such language.*',
        '(?i)\\bIs there anything else I can help you with\\?.*',
        '(?i)\\bCorrecting the translation to proper Dutch:.*',
        '(?i)\\bTheres more text to vertalen.*',
        '(?i)\\bmight affect.*',
        '(?i)\\bthe original text.*',
        '(?i)\\bthe naturalis.*'
    ]
    for pat in patterns:
        cleaned = re.sub(pat, '', cleaned)
    for l in keep_lines:
        if l not in cleaned:
            cleaned += '\n' + l
    cleaned = re.sub(r'\\s+', ' ', cleaned).strip()
    return cleaned


def levenshtein_distance(a, b):
    if a == b:
        return 0
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    v0 = list(range(len(b) + 1))
    v1 = [0] * (len(b) + 1)
    for i in range(len(a)):
        v1[0] = i + 1
        for j in range(len(b)):
            cost = 0 if a[i] == b[j] else 1
            v1[j + 1] = min(
                v1[j] + 1,
                v0[j + 1] + 1,
                v0[j] + cost
            )
        v0, v1 = v1, v0
    return v0[len(b)]


def choose_best_translation(candidate_translations, filter_config,
                            target_lang_name, original_text):
    if not candidate_translations:
        return ''
    valid_candidates = [fully_clean_subtitle_line(t).strip()
                        for t in candidate_translations if t.strip()]
    if not valid_candidates:
        return ''
    freq_map = {}
    for t in valid_candidates:
        freq_map[t] = freq_map.get(t, 0) + 1
    best = max(freq_map, key=freq_map.get)
    max_freq = freq_map[best]
    same_freq = [x for x in valid_candidates if freq_map[x] == max_freq]
    if len(same_freq) > 1:
        # Kies de tekst die het dichtst bij het origineel ligt (evt. heuristiek
        # per user)
        best = max(
            same_freq,
            key=lambda x: levenshtein_distance(
                x,
                original_text))
    return best


def finalize_result(raw_text, target_lang_name, filter_config,
                    parent_instance=None):
    text_no_disclaimers = remove_ai_disclaimers(raw_text)
    text_no_disclaimers = fully_clean_subtitle_line(text_no_disclaimers)
    spelled = correct_spelling(
        text_no_disclaimers,
        target_lang_name,
        parent_instance.settings if parent_instance else {},
        parent_instance
    )
    filtered = apply_filter_lists(spelled, filter_config)
    filtered = re.sub(r'\\s+', ' ', filtered).strip()
    return filtered


def export_subs(subs, filename):
    ext = os.path.splitext(filename)[1].lower()
    try:
        if ext == '.srt':
            subs.save(filename, format_='srt')
        elif ext == '.ass':
            subs.save(filename, format_='ass')
        elif ext == '.vtt':
            subs.save(filename, format_='vtt')
        elif ext == '.sub':
            subs.save(filename, format_='microdvd')
        else:
            subs.save(filename, format_='srt')
        return True, ''
    except Exception as e:
        return False, str(e)


def translate_with_server(server_name, text, source_lang_english,
                          target_lang_name, settings, filter_config,
                          model_file=None):
    target_english = LANGUAGE_PROMPT_MAP.get(target_lang_name, 'English')
    srv_cfg = settings['servers'].get(server_name, {})
    if not srv_cfg.get('active', False):
        return ''
    preprocessed_text = text
    if not preprocessed_text.strip():
        preprocessed_text = text
    try:
        if server_name == 'ollama':
            url = f"{srv_cfg['url']}:{srv_cfg['port']}/api/generate"
            prompt = f"""Please translate the following text from {source_lang_english} to {target_english} in a strictly natural way, without disclaimers or extra commentary:

{preprocessed_text}

Translated text:"""
            gpu_cfg = srv_cfg.get('gpu_support', {})
            gpu_enabled = gpu_cfg.get('enabled', False)
            extra_ollama_params = {}
            if gpu_enabled:
                num_gpu_layers = gpu_cfg.get('num_gpu_layers', 0)
                extra_ollama_params['num_gpu_layers'] = num_gpu_layers
                if gpu_cfg.get('gpu_memory'):
                    extra_ollama_params['gpu_memory'] = gpu_cfg['gpu_memory']
                if gpu_cfg.get('gpu_batch_size'):
                    extra_ollama_params['gpu_batch_size'] = gpu_cfg['gpu_batch_size']
            payload = {
                'model': settings.get('active_model', 'llama3:8b'),
                'prompt': prompt,
                'stream': False
            }
            if gpu_enabled:
                payload.update(extra_ollama_params)
            headers = {}
            ollama_key = srv_cfg.get('key', '')
            if ollama_key:
                headers['Authorization'] = f'Bearer {ollama_key}'
            resp = requests.post(
                url,
                json=payload,
                timeout=srv_cfg['timeout'],
                headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                return data.get('response', text).strip()

        elif server_name == 'deepl':
            key = srv_cfg.get('key', '')
            if key:
                base_url = 'https://api-free.deepl.com/v2/translate'
                lang_map = {
                    'Nederlands': 'NL',
                    'Engels': 'EN',
                    'Duits': 'DE',
                    'Frans': 'FR',
                    'Spaans': 'ES',
                    'Italiaans': 'IT',
                    'Portugees': 'PT',
                    'Pools': 'PL',
                    'Russisch': 'RU',
                    'Japans': 'JA',
                    'Chinees': 'ZH'
                }
                target_code = lang_map.get(target_lang_name, 'EN')
                resp = requests.post(
                    base_url,
                    data={
                        'auth_key': key,
                        'text': preprocessed_text,
                        'target_lang': target_code
                    },
                    timeout=srv_cfg['timeout']
                )
                if resp.status_code == 200:
                    data = resp.json()
                    if 'translations' in data and len(
                            data['translations']) > 0:
                        return data['translations'][0]['text'].strip()

        elif server_name == 'hugo':
            url = f"{srv_cfg['url']}:{srv_cfg['port']}/translate"
            payload = {
                'text': preprocessed_text,
                'source_language': source_lang_english,
                'target_language': target_english
            }
            resp = requests.post(url, json=payload, timeout=srv_cfg['timeout'])
            if resp.status_code == 200:
                data = resp.json()
                return data.get('translation', '').strip()
    except Exception as e:
        log_error(str(e), settings)
    return ''


class SubtitleTranslatorPro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.settings = load_settings()
        self.filters_config = load_filters_config()
        self.spellchecker = None

        self.title('Ondertitel Vertaler Pro - Compleet')
        self.geometry('1440x960')
        self.minsize(1000, 650)

        self.translating = threading.Event()
        self.spellcheck_stop_event = threading.Event()
        self.spellcheck_in_progress = threading.Event()
        self.auto_detect_enabled = True

        self.current_subs = None
        self.detected_language = None
        self.download_threads = {}
        self.status_var = tk.StringVar(value='Klaar')
        self.translated_subs = None
        self.spellchecked_subs = None

        self.font_family = tk.StringVar(
            value=self.settings.get(
                'font_family', 'Segoe UI'))
        self.font_size = tk.IntVar(value=self.settings.get('font_size', 12))
        self.text_style = tk.StringVar(
            value=self.settings.get(
                'text_style', 'normaal'))
        self.theme_var = tk.StringVar(
            value=self.settings.get(
                'theme', 'neo_dark'))
        self.target_lang_var = tk.StringVar(
            value=self.settings.get(
                'target_language', 'Nederlands'))
        self.source_lang_var = tk.StringVar(value='Automatisch')

        self.server_status_vars = {srv: tk.StringVar(
            value='Onbekend') for srv in self.settings['servers']}

        self.auto_scroll_enabled = True

        self.create_styles()
        self.create_widgets()
        self.apply_theme()

        self.theme_var.trace_add('write', self.change_theme_immediately)
        self.after(1000, self.periodic_server_status)

    def create_styles(self):
        THEMES = {
            'modern_black': {
                'bg': '#0a0a0a',
                'fg': '#ffffff',
                'accent': '#2563eb',
                'tab': '#1a1a1a',
                'entry_bg': '#181818',
                'entry_fg': '#ffffff',
                'button_fg': '#ffffff',
                'button_bg': '#2563eb',
                'button_active': '#174ea6',
                'red': '#e11d48',
                'blue': '#2563eb',
                'green': '#22c55e',
                'border': '#ffffff'
            },
            'modern_blue': {
                'bg': '#1e3a8a',
                'fg': '#ffffff',
                'accent': '#60a5fa',
                'tab': '#1e40af',
                'entry_bg': '#1e40af',
                'entry_fg': '#ffffff',
                'button_fg': '#ffffff',
                'button_bg': '#3b82f6',
                'button_active': '#2563eb',
                'red': '#ef4444',
                'blue': '#3b82f6',
                'green': '#06d6a0',
                'border': '#ffffff'
            },
            'neo_dark': {
                'bg': '#000000',
                'fg': '#39FF14',
                'accent': '#00FFFF',
                'tab': '#222222',
                'entry_bg': '#111111',
                'entry_fg': '#39FF14',
                'button_fg': '#000000',
                'button_bg': '#39FF14',
                'button_active': '#00FF7F',
                'red': '#FF0080',
                'blue': '#00FFFF',
                'green': '#00ff00',
                'border': '#39FF14'
            }
        }

        self.THEMES = THEMES
        self.THEMES.update(extra_neo_themes())

        style = ttk.Style(self)
        style.theme_use('clam')

        theme = THEMES.get(self.theme_var.get(), THEMES['neo_dark'])
        style.configure(
            'Blue.TButton',
            background=theme['button_bg'],
            foreground=theme['button_fg'],
            font=('Segoe UI', 10, 'bold'),
            padding=4
        )
        style.map(
            'Blue.TButton', background=[
                ('active', theme['button_active']), ('pressed', theme['button_active'])], foreground=[
                ('active', theme['button_fg'])])

        style.configure('Status.TLabel',
                        background=theme['bg'],
                        foreground=theme['fg'],
                        font=('Segoe UI', 9))

        style.configure(
            'blue.Horizontal.TProgressbar',
            troughcolor=theme['bg'],
            bordercolor=theme['bg'],
            background=theme['accent'] if 'accent' in theme else '#00FFFF',
            lightcolor=theme['accent'] if 'accent' in theme else '#00FFFF',
            darkcolor=theme['accent'] if 'accent' in theme else '#00FFFF')

    def change_theme_immediately(self, *args):
        self.settings['theme'] = self.theme_var.get()
        save_settings(self.settings)
        self.apply_theme()

    def get_font(self):
        style_map = {
            'normaal': ('normal', 'roman'),
            'vet': ('bold', 'roman'),
            'cursief': ('normal', 'italic'),
            'vet cursief': ('bold', 'italic'),
            'onderstreept': ('normal', 'roman', 'underline'),
            'vet onderstreept': ('bold', 'roman', 'underline'),
            'cursief onderstreept': ('normal', 'italic', 'underline'),
            'vet cursief onderstreept': ('bold', 'italic', 'underline')
        }
        style = self.text_style.get()
        font_family = self.font_family.get() or 'Segoe UI'
        font_size = self.font_size.get() or 12

        style_tuple = style_map.get(style, ('normal', 'roman'))
        weight = style_tuple[0] if len(style_tuple) > 0 else 'normal'
        slant = style_tuple[1] if len(style_tuple) > 1 else 'roman'
        underline = False
        if len(style_tuple) > 2 and 'underline' in style_tuple[2:]:
            underline = True
        if slant not in ('roman', 'italic'):
            slant = 'roman'
        if weight not in ('normal', 'bold'):
            weight = 'normal'
        return font.Font(family=font_family, size=font_size,
                         weight=weight, slant=slant, underline=underline)

    def apply_theme(self):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        self.configure(bg=theme['bg'])

        def apply_bg_recursively(parent):
            for w in parent.winfo_children():
                try:
                    w.configure(bg=theme['bg'])
                except BaseException:
                    pass
                apply_bg_recursively(w)

        apply_bg_recursively(self)

        style = ttk.Style(self)
        style.theme_use('clam')

        style.configure(
            'Blue.TButton',
            background=theme['button_bg'],
            foreground=theme['button_fg'],
            font=('Segoe UI', 10, 'bold'),
            padding=4
        )
        style.map('Blue.TButton',
                  background=[('active', theme['button_active']),
                              ('pressed', theme['button_active'])],
                  foreground=[('active', theme['button_fg'])])

        style.configure(
            'Status.TLabel',
            background=theme['bg'],
            foreground=theme['fg'],
            font=('Segoe UI', 9)
        )
        style.configure(
            'blue.Horizontal.TProgressbar',
            troughcolor=theme['bg'],
            bordercolor=theme['bg'],
            background=theme['accent'] if 'accent' in theme else '#00FFFF',
            lightcolor=theme['accent'] if 'accent' in theme else '#00FFFF',
            darkcolor=theme['accent'] if 'accent' in theme else '#00FFFF'
        )
        self.update_idletasks()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

        self.tab_translate = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_translate, text='Vertalen')
        self.create_translation_tab(self.tab_translate)

        self.tab_models = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_models, text='Modelbeheer')
        self.create_model_tab(self.tab_models)

        self.tab_servers = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_servers, text='Serverbeheer')
        self.create_server_tab(self.tab_servers)

        self.tab_info = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_info, text='Info')
        self.create_info_tab(self.tab_info)

        self.tab_filters = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_filters, text='Filters en lijsten')
        self.create_filters_and_lists_tab(self.tab_filters)

        self.tab_lijst_convertor = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_lijst_convertor, text='Lijst Convertor')
        self.create_list_converter_tab(self.tab_lijst_convertor)

        self.tab_spellcheck = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_spellcheck, text='Spellingcontrole')
        self.create_spellcheck_tab(self.tab_spellcheck)

        menubar = tk.Menu(self)
        bestand_menu = tk.Menu(menubar, tearoff=0)
        bestand_menu.add_command(
            label='Open ondertitel...',
            command=self.open_subtitle)
        bestand_menu.add_command(
            label='Opslaan als...',
            command=self.save_subtitle)
        bestand_menu.add_separator()

        # Nieuwe menu-optie voor script downloaden:
        bestand_menu.add_command(
            label='Script downloaden',
            command=self.download_script)

        bestand_menu.add_command(
            label='Foutlog wissen',
            command=lambda: clear_error_log(
                self.settings))
        bestand_menu.add_command(
            label='Foutlog opslaan als...',
            command=self.save_error_log)
        bestand_menu.add_separator()
        bestand_menu.add_command(label='Afsluiten', command=self.quit)
        menubar.add_cascade(label='Bestand', menu=bestand_menu)

        opties_menu = tk.Menu(menubar, tearoff=0)
        opties_menu.add_command(
            label='Instellingen',
            command=self.open_settings)
        opties_menu.add_command(
            label='Reset instellingen',
            command=self.reset_settings)
        menubar.add_cascade(label='Opties', menu=opties_menu)

        self.config(menu=menubar)

        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        statusbar = tk.Frame(self, height=24, bg=theme['bg'])
        statusbar.pack(fill=tk.X, side=tk.BOTTOM)
        self.status_label = ttk.Label(statusbar, textvariable=self.status_var,
                                      style='Status.TLabel', anchor='w')
        self.status_label.pack(side=tk.LEFT, padx=8)

    def periodic_server_status(self):
        self.check_server_status()
        self.after(5000, self.periodic_server_status)

    def create_translation_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])

        frame = tk.Frame(
            parent,
            bg=theme['bg'],
            highlightbackground=theme['border'],
            highlightthickness=4)
        frame.pack(fill=tk.BOTH, expand=True)

        topbar = tk.Frame(frame, bg=theme['bg'])
        topbar.pack(fill=tk.X, pady=(8, 8))

        ttk.Button(
            topbar,
            text='Vertalen starten',
            style='Blue.TButton',
            command=self.live_translate
        ).pack(side=tk.LEFT, padx=6, ipadx=8, ipady=2)

        ttk.Button(
            topbar,
            text='Stop vertalen',
            style='Blue.TButton',
            command=self.stop_translate
        ).pack(side=tk.LEFT, padx=6, ipadx=8, ipady=2)

        ttk.Button(
            topbar,
            text='Vertaling wissen',
            style='Blue.TButton',
            command=self.clear_translation
        ).pack(side=tk.LEFT, padx=6, ipadx=8, ipady=2)

        self.auto_scroll_btn = ttk.Button(
            topbar,
            text='Auto-scroll: Aan',
            style='Blue.TButton',
            command=self.toggle_auto_scroll
        )
        self.auto_scroll_btn.pack(side=tk.LEFT, padx=6, ipadx=8, ipady=2)

        self.auto_detect_btn = ttk.Button(
            topbar,
            text='Autom. taalherkenning: Aan',
            style='Blue.TButton',
            command=self.toggle_auto_detect
        )
        self.auto_detect_btn.pack(side=tk.LEFT, padx=6, ipadx=8, ipady=2)

        left = tk.Frame(
            frame,
            bg=theme['bg'],
            highlightbackground=theme['blue'],
            highlightthickness=2)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(
            left,
            text='Origineel',
            font=self.get_font(),
            bg=theme['bg'],
            fg=theme['fg']).pack(
            anchor='w')
        orig_scroll = tk.Scrollbar(left)
        orig_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_original = tk.Text(
            left,
            width=50,
            height=30,
            font=self.get_font(),
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['entry_fg'],
            highlightbackground=theme['border'],
            highlightthickness=2,
            yscrollcommand=orig_scroll.set
        )
        self.text_original.pack(fill=tk.BOTH, expand=True, pady=2)
        orig_scroll.config(command=self.text_original.yview)

        right = tk.Frame(
            frame,
            bg=theme['bg'],
            highlightbackground=theme['red'],
            highlightthickness=2)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(
            right,
            text='Vertaling',
            font=self.get_font(),
            bg=theme['bg'],
            fg=theme['fg']).pack(
            anchor='w')
        trans_scroll = tk.Scrollbar(right)
        trans_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_translation = tk.Text(
            right,
            width=50,
            height=30,
            font=self.get_font(),
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['entry_fg'],
            highlightbackground=theme['border'],
            highlightthickness=2,
            yscrollcommand=trans_scroll.set
        )
        self.text_translation.pack(fill=tk.BOTH, expand=True, pady=2)
        trans_scroll.config(command=self.text_translation.yview)

        bottom = tk.Frame(frame, bg=theme['bg'])
        bottom.pack(fill=tk.X, pady=4)

        tk.Label(
            bottom,
            text='Bron-taal:',
            bg=theme['bg'],
            fg=theme['fg']).pack(
            side=tk.LEFT,
            padx=4)
        LANGUAGES = [
            'Automatisch', 'Nederlands', 'Engels', 'Duits',
            'Frans', 'Spaans', 'Italiaans', 'Portugees',
            'Pools', 'Russisch', 'Japans', 'Chinees'
        ]
        self.source_lang_combo = ttk.Combobox(
            bottom, values=LANGUAGES, textvariable=self.source_lang_var, width=16)
        self.source_lang_combo.pack(side=tk.LEFT, padx=4)

        tk.Label(
            bottom,
            text='Doeltaal:',
            bg=theme['bg'],
            fg=theme['fg']).pack(
            side=tk.LEFT,
            padx=(
                16,
                4))
        target_languages = [
            'Nederlands', 'Engels', 'Duits',
            'Frans', 'Spaans', 'Italiaans', 'Portugees',
            'Pools', 'Russisch', 'Japans', 'Chinees'
        ]
        self.target_lang_combo = ttk.Combobox(
            bottom,
            values=target_languages,
            textvariable=self.target_lang_var,
            width=16)
        self.target_lang_combo.pack(side=tk.LEFT, padx=4)

        self.detect_once_button = ttk.Button(
            bottom,
            text='Detecteer bron-taal eenmalig',
            style='Blue.TButton',
            command=self.user_triggered_detect_language
        )
        self.detect_once_button.pack(side=tk.LEFT, padx=4, ipadx=4)

        self.text_original.bind(
            '<KeyRelease>',
            self.maybe_auto_detect_language)

        tk.Label(
            bottom,
            text='Tekststijl:',
            bg=theme['bg'],
            fg=theme['fg']).pack(
            side=tk.LEFT,
            padx=8)
        self.text_style_combo = ttk.Combobox(
            bottom,
            values=[
                'normaal',
                'vet',
                'cursief',
                'vet cursief',
                'onderstreept',
                'vet onderstreept',
                'cursief onderstreept',
                'vet cursief onderstreept'
            ],
            textvariable=self.text_style,
            width=18
        )
        self.text_style_combo.pack(side=tk.LEFT, padx=4)
        self.text_style_combo.bind(
            '<<ComboboxSelected>>',
            lambda e: self.update_fonts())

        tk.Label(
            bottom,
            text='Lettergrootte:',
            bg=theme['bg'],
            fg=theme['fg']).pack(
            side=tk.LEFT,
            padx=8)
        self.font_size_spin = tk.Spinbox(
            bottom,
            from_=8,
            to=48,
            textvariable=self.font_size,
            width=4,
            command=self.update_fonts)
        self.font_size_spin.pack(side=tk.LEFT, padx=4)
        self.font_size.trace('w', lambda *a: self.update_fonts())
        self.font_family.trace('w', lambda *a: self.update_fonts())

        progress_frame = tk.Frame(frame, bg=theme['bg'])
        progress_frame.pack(fill=tk.X, pady=(0, 6))
        self.progress_var = tk.DoubleVar(value=0)
        self.progress_label = tk.Label(
            progress_frame,
            text='0/0 regels vertaald',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font()
        )
        self.progress_label.pack(side=tk.LEFT, padx=8)
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            variable=self.progress_var,
            maximum=100,
            style='blue.Horizontal.TProgressbar')
        self.progress_bar.pack(fill=tk.X, expand=True, padx=8, side=tk.LEFT)

    def toggle_auto_scroll(self):
        self.auto_scroll_enabled = not self.auto_scroll_enabled
        self.auto_scroll_btn.config(
            text=f"Auto-scroll: {'Aan' if self.auto_scroll_enabled else 'Uit'}")
        self.status_var.set(
            f"Auto-scroll is {'ingeschakeld' if self.auto_scroll_enabled else 'uitgeschakeld'}."
        )

    def toggle_auto_detect(self):
        self.auto_detect_enabled = not self.auto_detect_enabled
        if self.auto_detect_enabled:
            self.auto_detect_btn.config(text='Autom. taalherkenning: Aan')
            self.status_var.set('Automatische taalherkenning is ingeschakeld.')
            self.auto_detect_language()
        else:
            self.auto_detect_btn.config(text='Autom. taalherkenning: Uit')
            self.status_var.set(
                'Automatische taalherkenning is uitgeschakeld.')

    def maybe_auto_detect_language(self, event=None):
        if self.auto_detect_enabled and self.source_lang_var.get() == 'Automatisch':
            txt = self.text_original.get('1.0', tk.END).strip()
            if len(txt) >= 30:
                self.auto_detect_language()

    def user_triggered_detect_language(self):
        if self.source_lang_var.get() != 'Automatisch':
            self.status_var.set("Bron-taal staat niet op 'Automatisch'.")
        else:
            self.auto_detect_language()

    def update_fonts(self, *args):
        f = self.get_font()
        self.text_original.configure(font=f)
        self.text_translation.configure(font=f)
        self.progress_label.configure(font=f)

    def auto_detect_language(self):
        text = self.text_original.get('1.0', tk.END).strip()
        if not text:
            self.status_var.set('Geen tekst om te detecteren.')
            return
        if len(text) < 30:
            self.status_var.set(
                'Tekst is te kort voor betrouwbare taalherkenning.')
            return
        try:
            code = detect_language_fallback(text)
            self.detected_language = code
            if self.detected_language:
                mapped_lang = map_detected_language_code(
                    self.detected_language)
                self.status_var.set(
                    f'Gedetecteerde taal: {mapped_lang} (code={code}).')
            else:
                self.status_var.set('Kon geen taal herkennen.')
        except BaseException:
            self.status_var.set('Taal niet herkend door langdetect.')

    def open_subtitle(self):
        filename = filedialog.askopenfilename(
            title='Open ondertitelbestand',
            filetypes=[
                ('Ondertiteling', '*.srt *.vtt *.ass *.sub *.sbv *.stl *.ssa *.txt'),
                ('Alle bestanden', '*.*')
            ]
        )
        if filename:
            try:
                subs = pysubs2.load(filename)
                self.current_subs = subs
                self.text_original.delete('1.0', tk.END)
                for i, line in enumerate(subs):
                    srt_line = f"""{i + 1}
{srt_time(line.start)} --> {srt_time(line.end)}
{line.text}

"""
                    self.text_original.insert(tk.END, srt_line)
                if self.auto_detect_enabled and self.source_lang_var.get() == 'Automatisch':
                    self.auto_detect_language()
                self.status_var.set(
                    f'Bestand geladen: {os.path.basename(filename)}')
            except Exception as e:
                messagebox.showerror('Fout', f'Fout bij laden: {e}')
                log_error(str(e), self.settings)
                self.status_var.set('Fout bij laden.')

    def save_subtitle(self):
        choice = messagebox.askyesno(
            'Opslaan',
            'Wil je het resultaat uit de Spellingcontrole-tab opslaan? (Ja = Spellingcontrole, Nee = Vertaling)'
        )
        filename = filedialog.asksaveasfilename(
            title='Opslaan als',
            defaultextension='.srt',
            filetypes=[
                ('SubRip (.srt)', '*.srt'),
                ('ASS (.ass)', '*.ass'),
                ('WebVTT (.vtt)', '*.vtt'),
                ('MicroDVD (.sub)', '*.sub'),
                ('Alle bestanden', '*.*')
            ]
        )
        if not filename:
            return

        if choice:
            # Gebruiker kiest "Ja" => Spellingcontrole-tab resultaat
            if not self.spellchecked_subs or len(self.spellchecked_subs) == 0:
                messagebox.showwarning(
                    'Geen data', 'Er zijn geen spelling-gecorrigeerde subs om op te slaan.')
                return
            success, err = export_subs(self.spellchecked_subs, filename)
        else:
            # Gebruiker kiest "Nee" => Vertaalde subs
            if not self.translated_subs or len(self.translated_subs) == 0:
                messagebox.showwarning(
                    'Geen data', 'Er zijn geen vertaalde subs om op te slaan.')
                return
            success, err = export_subs(self.translated_subs, filename)

        if success:
            messagebox.showinfo(
                'Opgeslagen',
                f'Bestand succesvol opgeslagen als {os.path.basename(filename)}.')
            self.status_var.set(
                f'Opgeslagen als: {os.path.basename(filename)}')
        else:
            messagebox.showerror('Fout', f'Fout bij opslaan: {err}')
            self.status_var.set('Fout bij opslaan.')

    def live_translate(self):
        if not self.current_subs:
            messagebox.showwarning(
                'Geen ondertitel',
                'Laad eerst een ondertitelbestand.')
            self.status_var.set('Geen ondertitel geladen.')
            return

        self.text_translation.delete('1.0', tk.END)
        target = self.target_lang_var.get()
        lines = list(self.current_subs)
        self.translating.set()
        total = len(lines)

        self.progress_var.set(0)
        self.progress_label.config(text=f'0/{total} regels vertaald')
        self.status_var.set(f'Vertalen gestart: 0/{total} regels.')

        self.translated_subs = pysubs2.SSAFile()

        # Eventueel bron-taal detecteren
        if self.source_lang_var.get() == 'Automatisch' and not self.detected_language:
            combined_text = '\n'.join([l.text for l in lines])
            if len(combined_text) > 30:
                try:
                    code = detect_language_fallback(combined_text)
                    if code:
                        self.detected_language = code
                except BaseException:
                    pass

        if self.source_lang_var.get() != 'Automatisch':
            source_lang_name = self.source_lang_var.get()
            source_english = LANGUAGE_PROMPT_MAP.get(
                source_lang_name, 'English')
        elif self.detected_language:
            mapped = map_detected_language_code(self.detected_language)
            source_english = LANGUAGE_PROMPT_MAP.get(mapped, 'English')
        else:
            source_english = 'English'

        def do_translate():
            servers_list = list(self.settings['servers'].keys())
            for idx, line in enumerate(lines):
                if not self.translating.is_set():
                    self.status_var.set('Live vertalen gestopt.')
                    return

                text_line_preprocessed = apply_filter_lists(
                    line.text, self.filters_config)
                if not text_line_preprocessed.strip():
                    text_line_preprocessed = line.text

                candidate_trans = []
                for srv_name in servers_list:
                    res = translate_with_server(
                        srv_name,
                        text_line_preprocessed,
                        source_english,
                        target,
                        self.settings,
                        self.filters_config
                    )
                    if res:
                        candidate_trans.append(res)

                if not candidate_trans:
                    final_translation_raw = text_line_preprocessed
                else:
                    final_translation_raw = choose_best_translation(
                        candidate_trans, self.filters_config, target, text_line_preprocessed)
                    if not final_translation_raw.strip():
                        final_translation_raw = text_line_preprocessed

                final_translation = finalize_result(
                    final_translation_raw, target, self.filters_config, self)
                srt_line = f"""{idx + 1}
{srt_time(line.start)} --> {srt_time(line.end)}
{final_translation}

"""
                self.text_translation.insert(tk.END, srt_line)

                new_line = line.copy()
                new_line.text = final_translation
                self.translated_subs.append(new_line)

                self.status_var.set(f'Live: Regel {idx + 1}/{total} vertaald.')
                self.progress_var.set((idx + 1) / total * 100)
                self.progress_label.config(
                    text=f'{idx + 1}/{total} regels vertaald')
                self.update_idletasks()

                if self.auto_scroll_enabled:
                    self.text_translation.yview_moveto(1)

            self.status_var.set(
                f'Live vertaling voltooid: {total}/{total} regels.')
            self.translating.clear()
            messagebox.showinfo('Vertaling klaar', 'De vertaling is voltooid!')

        threading.Thread(target=do_translate, daemon=True).start()

    def stop_translate(self):
        self.translating.clear()
        self.status_var.set('Live vertalen gestopt.')
        messagebox.showinfo('Stop vertalen', 'Live vertalen gestopt.')

    def clear_translation(self):
        self.text_translation.delete('1.0', tk.END)
        self.translated_subs = None
        self.status_var.set('Vertaling gewist.')

    def create_model_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.Frame(parent, bg=theme['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        tk.Label(
            frame,
            text='Modelbeheer',
            font=self.get_font(),
            bg=theme['bg'],
            fg=theme['fg']).pack(
            anchor='w',
            pady=2)

        self.model_listbox = tk.Listbox(
            frame,
            height=8,
            font=self.get_font(),
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            selectbackground=theme['accent']
        )
        self.model_listbox.pack(fill=tk.X, pady=2)
        self.refresh_model_list()

        btn_frame = tk.Frame(frame, bg=theme['bg'])
        btn_frame.pack(fill=tk.X, pady=6)

        def open_model_search():
            webbrowser.open_new('https://ollama.com/search')
            self.status_var.set(
                'Website https://ollama.com/search geopend in browser.')

        ttk.Button(
            btn_frame,
            text='Zoek modellen…',
            style='Blue.TButton',
            command=open_model_search).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Download + toevoegen (lokaal)',
            style='Blue.TButton',
            command=self.download_and_add_local).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Download + toevoegen (extern)',
            style='Blue.TButton',
            command=self.download_and_add_external).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Activeer model',
            style='Blue.TButton',
            command=self.activate_model_local).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Activeer model (extern)',
            style='Blue.TButton',
            command=self.activate_model_external).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Stop huidige model',
            style='Blue.TButton',
            command=self.stop_current_model).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Verwijderen',
            style='Blue.TButton',
            command=self.remove_model).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)

        ext_frame = tk.Frame(frame, bg=theme['bg'])
        ext_frame.pack(fill=tk.X, pady=(12, 2))

        tk.Label(
            ext_frame,
            text='Externe model-pad:',
            bg=theme['bg'],
            fg=theme['fg']).pack(
            side=tk.LEFT,
            padx=2)
        self.ext_model_dir_var = tk.StringVar(
            value=self.settings.get(
                'external_model_dir', ''))
        self.ext_model_entry = tk.Entry(
            ext_frame,
            textvariable=self.ext_model_dir_var,
            width=40,
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['entry_fg']
        )
        self.ext_model_entry.pack(side=tk.LEFT, padx=2)

        ttk.Button(
            ext_frame,
            text='Kies map',
            style='Blue.TButton',
            command=self.choose_external_directory).pack(
            side=tk.LEFT,
            padx=2)

        self.model_progress = tk.DoubleVar(value=0)
        self.model_progress_label = tk.Label(
            frame,
            text='Status: klaar',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font())
        self.model_progress_label.pack(fill=tk.X, padx=8, pady=(8, 2))
        self.progress_bar_models = ttk.Progressbar(
            frame, variable=self.model_progress, maximum=100)
        self.progress_bar_models.pack(fill=tk.X, pady=4)

    def stop_current_model(self):
        stop_all_model_servers(self.settings)
        self.status_var.set('Huidige modelserver is gestopt.')

    def refresh_model_list(self):
        self.model_listbox.delete(0, tk.END)
        for m in self.settings.get('models', []):
            self.model_listbox.insert(tk.END, m)
        if self.settings.get(
                'active_model') in self.settings.get('models', []):
            idx = self.settings['models'].index(self.settings['active_model'])
            self.model_listbox.selection_set(idx)

    def choose_external_directory(self):
        directory = filedialog.askdirectory(
            title='Kies een map op je externe schijf voor modellen'
        )
        if not directory:
            return
        try:
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
            modellen_subdir = os.path.join(directory, 'modellen')
            if not os.path.exists(modellen_subdir):
                os.makedirs(modellen_subdir, exist_ok=True)

            self.settings['external_model_dir'] = directory
            save_settings(self.settings)
            self.ext_model_dir_var.set(directory)
            messagebox.showinfo('Extern model-pad',
                                f'Extern model-pad ingesteld op:\n{directory}')
            self.status_var.set(f'Extern model-pad: {directory}')
        except Exception as e:
            messagebox.showerror('Fout', f'Fout bij instellen extern pad: {e}')
            log_error(str(e), self.settings)

    def download_and_add_local(self):
        model = simpledialog.askstring(
            'Model toevoegen (lokaal)',
            'Voer de naam van het model in:')
        if not model:
            return

        messagebox.showinfo('Download gestart',
                            f"Download van '{model}' (lokaal) gestart.")
        self.model_progress.set(0)
        self.model_progress_label.config(
            text=f"Download gestart voor '{model}' (lokaal)...")
        self.status_var.set(f"Download gestart voor '{model}' (lokaal)...")

        def do_download_local():
            try:
                url = f"{self.settings['servers']['ollama']['url']}:{self.settings['servers']['ollama']['port']}/api/pull"
                resp = requests.post(
                    url,
                    json={
                        'name': model},
                    stream=True,
                    timeout=600)
                if resp.status_code != 200:
                    raise Exception(f'Server gaf status {resp.status_code}')

                model_path = os.path.join(MODELS_DIR_DEFAULT, model + '.bin')
                with open(model_path, 'wb') as f:
                    chunk_count = 0
                    for chunk in resp.iter_content(chunk_size=8192):
                        if not chunk:
                            continue
                        f.write(chunk)
                        chunk_count += 1
                        if chunk_count % 50 == 0:
                            self.model_progress.set(
                                min(100, self.model_progress.get() + 3))
                            self.model_progress_label.config(
                                text=f"Download '{model}' (lokaal) ~{self.model_progress.get():.1f}%")
                            self.update_idletasks()

                if model not in self.settings['models']:
                    self.settings['models'].append(model)
                save_settings(self.settings)
                self.refresh_model_list()

                self.status_var.set(
                    f"Model '{model}' succesvol gedownload (lokaal).")
                self.model_progress_label.config(
                    text=f"Model '{model}' succesvol gedownload (lokaal)."
                )
                messagebox.showinfo(
                    'Download voltooid',
                    f"Model '{model}' is lokaal toegevoegd.")
            except Exception as e:
                self.status_var.set(f'Fout bij downloaden: {e}')
                self.model_progress_label.config(
                    text=f'Fout bij downloaden: {e}')
                log_error(str(e), self.settings)
                messagebox.showerror('Download', f'Fout bij downloaden: {e}')
            self.model_progress.set(0)

        t = threading.Thread(target=do_download_local, daemon=True)
        self.download_threads[model] = t
        t.start()

    def download_and_add_external(self):
        if not self.settings.get('external_model_dir'):
            messagebox.showwarning(
                'Geen externe map',
                'Stel eerst het externe model-pad in.')
            return

        model = simpledialog.askstring(
            'Model toevoegen (extern)',
            'Voer de naam van het model in:')
        if not model:
            return

        messagebox.showinfo('Download gestart',
                            f"Download van '{model}' (extern) gestart.")
        self.model_progress.set(0)
        self.model_progress_label.config(
            text=f"Download gestart voor '{model}' (extern)...")
        self.status_var.set(f"Download gestart voor '{model}' (extern)...")

        def do_download_external():
            try:
                url = f"{self.settings['servers']['ollama']['url']}:{self.settings['servers']['ollama']['port']}/api/pull"
                resp = requests.post(
                    url,
                    json={
                        'name': model},
                    stream=True,
                    timeout=600)
                if resp.status_code != 200:
                    raise Exception(f'Server gaf status {resp.status_code}')

                ext_dir = os.path.join(
                    self.settings['external_model_dir'], 'modellen')
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir, exist_ok=True)

                model_path = os.path.join(ext_dir, model + '.bin')
                with open(model_path, 'wb') as f:
                    chunk_count = 0
                    for chunk in resp.iter_content(chunk_size=8192):
                        if not chunk:
                            continue
                        f.write(chunk)
                        chunk_count += 1
                        if chunk_count % 50 == 0:
                            self.model_progress.set(
                                min(100, self.model_progress.get() + 3))
                            self.model_progress_label.config(
                                text=f"Download '{model}' (extern) ~{self.model_progress.get():.1f}%")
                            self.update_idletasks()

                if model not in self.settings['models']:
                    self.settings['models'].append(model)
                save_settings(self.settings)
                self.refresh_model_list()

                self.status_var.set(
                    f"Model '{model}' succesvol gedownload (extern).")
                self.model_progress_label.config(
                    text=f"Model '{model}' succesvol gedownload (extern)."
                )
                messagebox.showinfo(
                    'Download voltooid',
                    f"Model '{model}' is extern toegevoegd.")
            except Exception as e:
                self.status_var.set(f'Fout bij downloaden: {e}')
                self.model_progress_label.config(
                    text=f'Fout bij downloaden: {e}')
                log_error(str(e), self.settings)
                messagebox.showerror('Download', f'Fout bij downloaden: {e}')
            self.model_progress.set(0)

        t = threading.Thread(target=do_download_external, daemon=True)
        self.download_threads[model] = t
        t.start()

    def activate_model_local(self):
        sel = self.model_listbox.curselection()
        if not sel:
            messagebox.showwarning(
                'Selecteer model',
                'Selecteer een model om lokaal te activeren.')
            return
        model = self.model_listbox.get(sel[0])
        self.model_progress_label.config(
            text=f"Model '{model}' activeren (lokaal)...")
        self.settings['active_model'] = model
        save_settings(self.settings)
        self.refresh_model_list()
        messagebox.showinfo(
            'Activeren',
            f"Model '{model}' is nu actief (lokaal).")
        self.status_var.set(f"Model '{model}' is nu actief (lokaal).")
        self.model_progress_label.config(
            text=f"Model '{model}' is nu actief (lokaal).")

    def activate_model_external(self):
        if not self.settings.get('external_model_dir'):
            messagebox.showwarning(
                'Geen externe map',
                'Stel eerst een extern model-pad in.')
            return
        sel = self.model_listbox.curselection()
        if not sel:
            messagebox.showwarning(
                'Selecteer model',
                'Selecteer een model om extern te activeren.')
            return
        model = self.model_listbox.get(sel[0])
        ext_dir = os.path.join(self.settings['external_model_dir'], 'modellen')
        ext_file = os.path.join(ext_dir, model + '.bin')
        if not os.path.exists(ext_file):
            msg = f"""Het geselecteerde model '{model}' lijkt niet te bestaan in:
{ext_file}

We activeren het toch in de software, maar het bestand ontbreekt mogelijk."""
            messagebox.showwarning('Model extern niet gevonden', msg)

        self.settings['active_model'] = model
        save_settings(self.settings)
        self.refresh_model_list()
        messagebox.showinfo(
            'Externe model activeren',
            f"Model '{model}' is nu actief (extern).")
        self.status_var.set(f"Model '{model}' is nu actief (extern).")
        self.model_progress_label.config(
            text=f"Model '{model}' extern actief.")

    def remove_model(self):
        sel = self.model_listbox.curselection()
        if not sel:
            messagebox.showwarning(
                'Selecteer model',
                'Selecteer een model om te verwijderen.')
            return
        model = self.model_listbox.get(sel[0])
        if model in self.settings['models']:
            self.settings['models'].remove(model)
        if self.settings.get('active_model') == model:
            self.settings['active_model'] = ''
        save_settings(self.settings)
        self.refresh_model_list()

        try:
            model_file = os.path.join(MODELS_DIR_DEFAULT, model + '.bin')
            if os.path.exists(model_file):
                os.remove(model_file)
        except BaseException:
            pass
        try:
            ext_dir = self.settings.get('external_model_dir')
            if ext_dir:
                modellen_ext_dir = os.path.join(ext_dir, 'modellen')
                external_file = os.path.join(modellen_ext_dir, model + '.bin')
                if os.path.exists(external_file):
                    os.remove(external_file)
        except BaseException:
            pass

        messagebox.showinfo('Verwijderen', f"Model '{model}' verwijderd.")
        self.status_var.set(f"Model '{model}' verwijderd.")
        self.model_progress_label.config(text=f"Model '{model}' verwijderd.")

    def create_server_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.Frame(parent, bg=theme['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        tk.Label(
            frame,
            text='Serverbeheer',
            font=self.get_font(),
            bg=theme['bg'],
            fg=theme['fg']).pack(
            anchor='w',
            pady=2)

        self.server_vars = {}
        self.timeout_vars = {}
        self.url_vars = {}
        self.port_vars = {}
        self.server_entries = []
        self.ollama_gpu_enabled_vars = {}
        self.ollama_gpu_layers_vars = {}
        self.ollama_gpu_memory_vars = {}
        self.ollama_gpu_batch_vars = {}

        for srv in self.settings['servers']:
            var = tk.BooleanVar(value=self.settings['servers'][srv]['active'])
            self.server_vars[srv] = var

            row = tk.Frame(
                frame,
                bg=theme['bg'],
                highlightbackground=theme['border'],
                highlightthickness=1)
            row.pack(fill=tk.X, pady=4, padx=4)

            cb = ttk.Checkbutton(
                row, text=f'{srv.capitalize()} aan/uit', variable=var)
            cb.pack(side=tk.LEFT, padx=5)

            tk.Label(
                row,
                text='Status:',
                bg=theme['bg'],
                fg=theme['fg']).pack(
                side=tk.LEFT)
            lbl = tk.Label(row,
                           textvariable=self.server_status_vars[srv],
                           fg='green' if var.get() else 'red',
                           bg=theme['bg'])
            lbl.pack(side=tk.LEFT, padx=5)

            if srv in ['deepl', 'ollama']:
                tk.Label(
                    row,
                    text='API sleutel:',
                    bg=theme['bg'],
                    fg=theme['fg']).pack(
                    side=tk.LEFT,
                    padx=2)
                key_var = tk.StringVar(
                    value=self.settings['servers'][srv].get(
                        'key', ''))
                self.url_vars[srv] = key_var
                key_entry = tk.Entry(
                    row,
                    textvariable=key_var,
                    width=24,
                    bg=theme['entry_bg'],
                    fg=theme['entry_fg'],
                    insertbackground=theme['entry_fg']
                )
                key_entry.pack(side=tk.LEFT)
                self.server_entries.append((srv, 'key', key_var))

            if srv not in ['deepl']:
                tk.Label(
                    row,
                    text='URL:',
                    bg=theme['bg'],
                    fg=theme['fg']).pack(
                    side=tk.LEFT,
                    padx=2)
                url_var = tk.StringVar(
                    value=self.settings['servers'][srv].get(
                        'url', 'http://127.0.0.1'))
                self.url_vars[srv] = url_var
                url_entry = tk.Entry(
                    row,
                    textvariable=url_var,
                    width=16,
                    bg=theme['entry_bg'],
                    fg=theme['entry_fg'],
                    insertbackground=theme['entry_fg']
                )
                url_entry.pack(side=tk.LEFT)
                self.server_entries.append((srv, 'url', url_var))

                tk.Label(
                    row,
                    text='Poort:',
                    bg=theme['bg'],
                    fg=theme['fg']).pack(
                    side=tk.LEFT,
                    padx=2)
                port_var = tk.IntVar(
                    value=self.settings['servers'][srv].get(
                        'port', 0))
                self.port_vars[srv] = port_var
                port_entry = tk.Entry(
                    row,
                    textvariable=port_var,
                    width=6,
                    bg=theme['entry_bg'],
                    fg=theme['entry_fg'],
                    insertbackground=theme['entry_fg']
                )
                port_entry.pack(side=tk.LEFT)
                self.server_entries.append((srv, 'port', port_var))

            tk.Label(
                row,
                text='Timeout:',
                bg=theme['bg'],
                fg=theme['fg']).pack(
                side=tk.LEFT,
                padx=2)
            timeout_var = tk.IntVar(
                value=self.settings['servers'][srv].get(
                    'timeout', 30))
            self.timeout_vars[srv] = timeout_var
            entry = tk.Entry(
                row,
                textvariable=timeout_var,
                width=5,
                bg=theme['entry_bg'],
                fg=theme['entry_fg'],
                insertbackground=theme['entry_fg']
            )
            entry.pack(side=tk.LEFT)
            self.server_entries.append((srv, 'timeout', timeout_var))

            if srv == 'ollama':
                gpu_frame = tk.Frame(row, bg=theme['bg'])
                gpu_frame.pack(side=tk.LEFT, padx=4)

                gpu_enabled_var = tk.BooleanVar(
                    value=self.settings['servers']['ollama']['gpu_support'].get(
                        'enabled', False))
                self.ollama_gpu_enabled_vars[srv] = gpu_enabled_var
                gpu_cb = ttk.Checkbutton(
                    gpu_frame, text='GPU?', variable=gpu_enabled_var)
                gpu_cb.pack(side=tk.LEFT, padx=2)

                gpu_layers_var = tk.IntVar(
                    value=self.settings['servers']['ollama']['gpu_support'].get(
                        'num_gpu_layers', 0))
                self.ollama_gpu_layers_vars[srv] = gpu_layers_var
                tk.Label(
                    gpu_frame,
                    text='Layers:',
                    bg=theme['bg'],
                    fg=theme['fg']).pack(
                    side=tk.LEFT,
                    padx=2)
                layers_entry = tk.Entry(
                    gpu_frame,
                    textvariable=gpu_layers_var,
                    width=5,
                    bg=theme['entry_bg'],
                    fg=theme['entry_fg'],
                    insertbackground=theme['entry_fg']
                )
                layers_entry.pack(side=tk.LEFT)

                gpu_mem_var = tk.StringVar(
                    value=self.settings['servers']['ollama']['gpu_support'].get(
                        'gpu_memory', 'auto'))
                self.ollama_gpu_memory_vars[srv] = gpu_mem_var
                tk.Label(
                    gpu_frame,
                    text='Mem:',
                    bg=theme['bg'],
                    fg=theme['fg']).pack(
                    side=tk.LEFT,
                    padx=2)
                gpu_mem_combo = ttk.Combobox(
                    gpu_frame,
                    textvariable=gpu_mem_var,
                    values=[
                        'auto',
                        '4GB',
                        '6GB',
                        '8GB',
                        '12GB',
                        '16GB',
                        '24GB',
                        '32GB'],
                    width=6)
                gpu_mem_combo.pack(side=tk.LEFT)

                gpu_batch_var = tk.IntVar(
                    value=self.settings['servers']['ollama']['gpu_support'].get(
                        'gpu_batch_size', 512))
                self.ollama_gpu_batch_vars[srv] = gpu_batch_var
                tk.Label(
                    gpu_frame,
                    text='Batch:',
                    bg=theme['bg'],
                    fg=theme['fg']).pack(
                    side=tk.LEFT,
                    padx=2)
                batch_entry = tk.Entry(
                    gpu_frame,
                    textvariable=gpu_batch_var,
                    width=5,
                    bg=theme['entry_bg'],
                    fg=theme['entry_fg'],
                    insertbackground=theme['entry_fg']
                )
                batch_entry.pack(side=tk.LEFT)

        ttk.Button(
            frame,
            text='Status controleren',
            style='Blue.TButton',
            command=self.check_server_status).pack(
            anchor='w',
            padx=5,
            pady=5)

        self.server_status_label = tk.Label(
            frame,
            text='Statuscontrole: niet gestart',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font()
        )
        self.server_status_label.pack(fill=tk.X, padx=8, pady=(2, 0))

        ttk.Button(
            frame,
            text='Opslaan',
            style='Blue.TButton',
            command=self.save_server_settings).pack(
            anchor='w',
            padx=5,
            pady=5)

        ttk.Button(
            frame,
            text='NOODSTOP: Stop ALLES',
            style='Blue.TButton',
            command=lambda: stop_all_model_servers(self.settings)
        ).pack(anchor='w', padx=5, pady=10)

    def save_server_settings(self):
        for srv in self.settings['servers']:
            self.settings['servers'][srv]['active'] = self.server_vars[srv].get()

        for srv, typ, var in self.server_entries:
            if typ == 'url':
                self.settings['servers'][srv]['url'] = var.get()
            elif typ == 'port':
                try:
                    self.settings['servers'][srv]['port'] = int(var.get())
                except BaseException:
                    self.status_var.set('Ongeldige poort waarde.')
            elif typ == 'key':
                self.settings['servers'][srv]['key'] = var.get()
            elif typ == 'timeout':
                try:
                    self.settings['servers'][srv]['timeout'] = int(var.get())
                except BaseException:
                    self.status_var.set('Ongeldige timeout waarde.')

        ollama_cfg = self.settings['servers'].get('ollama', {})
        if 'gpu_support' not in ollama_cfg:
            ollama_cfg['gpu_support'] = {}
        ollama_cfg['gpu_support']['enabled'] = self.ollama_gpu_enabled_vars['ollama'].get()
        ollama_cfg['gpu_support']['num_gpu_layers'] = self.ollama_gpu_layers_vars['ollama'].get()
        ollama_cfg['gpu_support']['gpu_memory'] = self.ollama_gpu_memory_vars['ollama'].get()
        ollama_cfg['gpu_support']['gpu_batch_size'] = self.ollama_gpu_batch_vars['ollama'].get()

        save_settings(self.settings)
        messagebox.showinfo(
            'Serverbeheer',
            'Serverinstellingen (inclusief GPU-instellingen) opgeslagen.')
        self.status_var.set('Serverinstellingen opgeslagen.')
        self.check_server_status()

    def check_server_status(self):
        self.server_status_label.config(text='Statuscontrole bezig...')

        def do_check():
            for srv in self.settings['servers']:
                status = self.get_server_status(srv)
                self.server_status_vars[srv].set(status)
            self.status_var.set('Serverstatus gecontroleerd.')
            self.server_status_label.config(text='Statuscontrole voltooid!')

        threading.Thread(target=do_check, daemon=True).start()

    def get_server_status(self, srv):
        try:
            if not self.settings['servers'][srv]['active']:
                return 'Uit'
            if srv == 'ollama':
                url = f"{self.settings['servers'][srv]['url']}:{self.settings['servers'][srv]['port']}/api/tags"
                resp = requests.get(url, timeout=3)
                return 'Online' if resp.status_code == 200 else 'Offline'
            elif srv == 'deepl':
                key = self.settings['servers'][srv]['key']
                if not key:
                    return 'Geen sleutel'
                dd_url = 'https://api-free.deepl.com/v2/usage'
                resp = requests.get(
                    dd_url, params={
                        'auth_key': key}, timeout=3)
                return 'Online' if resp.status_code == 200 else 'Offline'
            elif srv == 'hugo':
                url = f"{self.settings['servers'][srv]['url']}:{self.settings['servers'][srv]['port']}/status"
                resp = requests.get(url, timeout=3)
                return 'Online' if resp.status_code == 200 else 'Offline'
            return 'Onbekend'
        except BaseException:
            return 'Offline'

    def create_info_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.Frame(parent, bg=theme['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=16)

        tk.Label(
            frame,
            text='Informatie & Installatie',
            font=self.get_font(),
            bg=theme['bg'],
            fg=theme['accent']
        ).pack(anchor='w', pady=(0, 8))

        info_texts = [
            ('Ollama (server, modellen):', 'https://ollama.com/'),
            ('DeepL API (vertaling):', 'https://www.deepl.com/pro-api'),
            ('HuggingFace (modellen):', 'https://huggingface.co/models'),
            ('OpenAI GPT (API):', 'https://platform.openai.com/'),
            ('Llama 2 (Meta, download):', 'https://ai.meta.com/resources/models-and-libraries/llama-downloads/'),
            ('Mistral AI (modellen):', 'https://mistral.ai/news/announcing-mistral-7b/'),
            ('Google Translate API:', 'https://cloud.google.com/translate'),
            ('Meer info over SRT/ASS/VTT:', 'https://en.wikipedia.org/wiki/SubRip')
        ]
        for label, url in info_texts:
            row = tk.Frame(frame, bg=theme['bg'])
            row.pack(anchor='w', pady=2, fill=tk.X)

            lbl = tk.Label(
                row,
                text=label,
                font=self.get_font(),
                bg=theme['bg'],
                fg=theme['fg'],
                cursor='hand2')
            lbl.pack(side=tk.LEFT)
            link = tk.Label(
                row,
                text=url,
                font=self.get_font(),
                fg=theme['accent'],
                bg=theme['bg'],
                cursor='hand2',
                underline=True)
            link.pack(side=tk.LEFT, padx=6)

            def open_url(link_url=url):
                webbrowser.open_new(link_url)

            link.bind('<Button-1>', lambda e, link_url=url: open_url(link_url))

        tk.Label(
            frame,
            text='Gebruik steeds de officiële sites voor installatie en modeldownloads.',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font()).pack(
            anchor='w',
            pady=(
                12,
                0))

    def create_filters_and_lists_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        canvas = tk.Canvas(parent, bg=theme['bg'], highlightthickness=0)
        scroll_y = tk.Scrollbar(
            parent,
            orient='vertical',
            command=canvas.yview)
        self.filters_container = tk.Frame(canvas, bg=theme['bg'])
        self.filters_container.bind(
            '<Configure>', lambda e: canvas.configure(
                scrollregion=canvas.bbox('all')))

        canvas.create_window(
            (0, 0), window=self.filters_container, anchor='nw')
        canvas.configure(yscrollcommand=scroll_y.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        instruction_label = tk.Label(
            self.filters_container,
            text="""Configureer filter en lijsten:
• Schakel lijsten in/uit voor woordvervanging.
• Voeg evt. eigen termen of zinnen toe.
• Met 'Bewerk' kun je items direct wijzigen.
• Hoofdschakelaar voor filters staat onderaan.""",
            bg=theme['bg'],
            fg=theme['green'],
            justify=tk.LEFT,
            font=self.get_font()
        )
        instruction_label.pack(anchor='w', padx=8, pady=8)

        self.filter_enabled_var = tk.BooleanVar(
            value=self.filters_config.get(
                'filters_enabled', True))
        main_chk_frame = tk.Frame(self.filters_container, bg=theme['bg'])
        main_chk_frame.pack(fill=tk.X, padx=8)

        main_filter_chk = ttk.Checkbutton(
            main_chk_frame,
            text='Volledige filter actief (strikte vervangingen)',
            variable=self.filter_enabled_var,
            command=self.toggle_main_filter
        )
        main_filter_chk.pack(anchor='w', pady=4)

        self.lists_frame = tk.Frame(self.filters_container, bg=theme['bg'])
        self.lists_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=4)

        self.create_paste_and_save_section()

        bottom_bar = tk.Frame(self.filters_container, bg=theme['bg'])
        bottom_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=8, padx=8)

        ttk.Button(
            bottom_bar,
            text='Nieuwe lijst aanmaken',
            style='Blue.TButton',
            command=self.add_new_list
        ).pack(side=tk.LEFT, padx=4)

        ttk.Button(
            bottom_bar,
            text='Opslaan filterinstellingen',
            style='Blue.TButton',
            command=self.save_filter_settings
        ).pack(side=tk.LEFT, padx=4)

        self.populate_lists_ui()

    def create_paste_and_save_section(self):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.LabelFrame(
            self.filters_container,
            text='Tekst plakken en opslaan',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font()
        )
        frame.pack(fill=tk.X, padx=8, pady=8)

        label = tk.Label(
            frame,
            text='Plak hieronder vrije tekst en kies een bestandsformaat:',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font()
        )
        label.pack(anchor='w', padx=4, pady=(4, 2))

        scroll_text_frame = tk.Frame(frame, bg=theme['bg'])
        scroll_text_frame.pack(fill=tk.X, padx=4, pady=2)

        self.paste_textbox = tk.Text(
            scroll_text_frame,
            height=8,
            font=self.get_font(),
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['entry_fg']
        )
        self.paste_textbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        text_scroll = tk.Scrollbar(
            scroll_text_frame,
            command=self.paste_textbox.yview)
        text_scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.paste_textbox.configure(yscrollcommand=text_scroll.set)

        format_label = tk.Label(
            frame,
            text='Formaat:',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font())
        format_label.pack(side=tk.LEFT, padx=(4, 0))

        self.save_format_var = tk.StringVar(value='.srt')
        formats = ['.srt', '.txt', '.json', '.ass', '.vtt']
        format_combo = ttk.Combobox(
            frame,
            values=formats,
            textvariable=self.save_format_var,
            width=6)
        format_combo.pack(side=tk.LEFT, padx=4)

        save_button = ttk.Button(
            frame,
            text='Opslaan',
            style='Blue.TButton',
            command=self.paste_and_save_text)
        save_button.pack(side=tk.LEFT, padx=4, pady=(0, 4))

    def paste_and_save_text(self):
        text_content = self.paste_textbox.get('1.0', tk.END).strip()
        if not text_content:
            messagebox.showwarning('Lege tekst', 'Geen tekst om op te slaan.')
            return
        extension = self.save_format_var.get()

        filename = filedialog.asksaveasfilename(
            title='Tekst opslaan als',
            defaultextension=extension,
            filetypes=[
                ('SRT-bestand', '*.srt'),
                ('Tekstbestand', '*.txt'),
                ('JSON-bestand', '*.json'),
                ('ASS-bestand', '*.ass'),
                ('WebVTT-bestand', '*.vtt'),
                ('Alle bestanden', '*.*')
            ]
        )
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text_content)
                messagebox.showinfo(
                    'Opgeslagen',
                    f'Tekst succesvol opgeslagen als {os.path.basename(filename)}')
                self.status_var.set(
                    f'Tekst succesvol opgeslagen als {os.path.basename(filename)}'
                )
            except Exception as e:
                messagebox.showerror('Fout', f'Fout bij opslaan: {e}')
                self.status_var.set(f'Fout bij opslaan: {e}')

    # ---------------------- (EINDE) Tekst plakken en opslaan ----------------

    # -------- Hieronder extra tabbladen voor Lijst Convertor en Spellingcontr
    def create_list_converter_tab(self, parent):
        # Placeholder voor de tab 'Lijst Convertor'
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.Frame(parent, bg=theme['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        tk.Label(
            frame,
            text='Hier kun je lijsten converteren.',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font()).pack()

    def create_spellcheck_tab(self, parent):
        # Placeholder voor de tab 'Spellingcontrole'
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.Frame(parent, bg=theme['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        tk.Label(frame, text='Hier kun je spellingcontrole uitvoeren.',
                 bg=theme['bg'], fg=theme['fg'], font=self.get_font()).pack()

    def populate_lists_ui(self):
        for child in self.lists_frame.winfo_children():
            child.destroy()
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])

        for idx, list_data in enumerate(self.filters_config.get('lists', [])):
            list_panel = tk.LabelFrame(
                self.lists_frame,
                text=list_data['name'],
                bg=theme['bg'],
                fg=theme['fg'],
                font=self.get_font()
            )
            list_panel.pack(fill=tk.X, expand=False, pady=4, padx=4)

            top_list_bar = tk.Frame(list_panel, bg=theme['bg'])
            top_list_bar.pack(fill=tk.X, pady=2)

            enabled_var = tk.BooleanVar(value=list_data.get('enabled', False))
            chk_btn = ttk.Checkbutton(
                top_list_bar,
                text=f"Aan/uit voor '{list_data['name']}'",
                variable=enabled_var,
                command=lambda v=enabled_var,
                i=idx: self.toggle_list_enabled(
                    i,
                    v))
            chk_btn.pack(side=tk.LEFT, padx=4)

            tk.Label(
                top_list_bar,
                text='URL:',
                bg=theme['bg'],
                fg=theme['fg']).pack(
                side=tk.LEFT,
                padx=4)
            url_var = tk.StringVar(value=list_data.get('source_url', ''))
            url_entry = tk.Entry(
                top_list_bar,
                textvariable=url_var,
                width=50,
                bg=theme['entry_bg'],
                fg=theme['entry_fg'],
                insertbackground=theme['entry_fg']
            )
            url_entry.pack(side=tk.LEFT, padx=2)

            def save_list_url(list_index=idx, var=url_var):
                self.filters_config['lists'][list_index]['source_url'] = var.get(
                )
                self.status_var.set(
                    f"Bron-URL opgeslagen voor lijst '{self.filters_config['lists'][list_index]['name']}'."
                )

            btn_save_url = ttk.Button(
                top_list_bar,
                text='Opslaan',
                style='Blue.TButton',
                command=save_list_url
            )
            btn_save_url.pack(side=tk.LEFT, padx=2)

            def open_list_url(uvar=url_var):
                if uvar.get():
                    webbrowser.open_new(uvar.get())

            btn_open_url = ttk.Button(
                top_list_bar,
                text='Openen',
                style='Blue.TButton',
                command=open_list_url)
            btn_open_url.pack(side=tk.LEFT, padx=2)

    def toggle_list_enabled(self, list_index, var):
        self.filters_config['lists'][list_index]['enabled'] = var.get()
        self.status_var.set(
            f"Filterlijst '{self.filters_config['lists'][list_index]['name']}' is nu "
            f"{'ingeschakeld' if var.get() else 'uitgeschakeld'}.")

    def save_filter_settings(self):
        self.filters_config['filters_enabled'] = self.filter_enabled_var.get()
        save_filters_config(self.filters_config)
        messagebox.showinfo('Filters', 'Filterconfiguratie opgeslagen.')
        self.status_var.set('Filterconfiguratie opgeslagen.')

    def toggle_main_filter(self):
        self.filters_config['filters_enabled'] = self.filter_enabled_var.get()
        self.status_var.set(
            f"Filter is nu {'ingeschakeld' if self.filter_enabled_var.get() else 'uitgeschakeld'}."
        )

    def add_new_list(self):
        name = simpledialog.askstring('Nieuwe lijst', 'Naam van de lijst:')
        if not name:
            return
        new_list = {
            'name': name,
            'enabled': False,
            'file_format': 'json',
            'source_url': '',
            'priority': len(self.filters_config.get('lists', [])) + 1,
            'items': {}
        }
        self.filters_config['lists'].append(new_list)
        self.populate_lists_ui()
        self.status_var.set(f"Nieuwe filterlijst '{name}' is aangemaakt.")

    def download_script(self):
        """
        Download steeds het originele script vanaf GitHub, alleen toegankelijk na admin-wachtwoord.
        """
        pw = simpledialog.askstring(
            'Admin Password',
            'Geef het Admin-wachtwoord om het script te downloaden:',
            show='*'
        )
        if not pw:
            messagebox.showwarning(
                'Afgebroken', 'Download geannuleerd door gebruiker.')
            return

        if not check_admin_password(pw):
            messagebox.showerror(
                'Ongeldig wachtwoord',
                'Admin-wachtwoord is onjuist. Toegang geweigerd.')
            return

        filename = filedialog.asksaveasfilename(
            title='Script opslaan als',
            defaultextension='.py',
            filetypes=[("Python Script", "*.py"), ("Alle bestanden", "*.*")]
        )
        if not filename:
            self.status_var.set(
                "Download script geannuleerd (geen bestand gekozen).")
            return

        self.status_var.set("Script downloaden van GitHub...")
        try:
            resp = requests.get(GITHUB_SCRIPT_URL, timeout=20)
            if resp.status_code != 200:
                messagebox.showerror(
                    "Fout", f"Server gaf HTTP {resp.status_code}")
                self.status_var.set(
                    f"Download script mislukt: HTTP {resp.status_code}")
                return

            script_content = resp.text
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(script_content)

            messagebox.showinfo(
                "Succes", f"Script gedownload en opgeslagen als {os.path.basename(filename)}")
            self.status_var.set(
                f"Script gedownload en opgeslagen als {os.path.basename(filename)}"
            )
        except Exception as e:
            messagebox.showerror('Fout', f'Fout bij laden: {e}')
            log_error(str(e), self.settings)
            self.status_var.set('Fout bij laden.')

    def save_error_log(self):
        filename = filedialog.asksaveasfilename(
            title='Foutlog opslaan als', defaultextension='.log', filetypes=[
                ('Log bestanden', '*.log'), ('Tekst bestanden', '*.txt'), ('Alle bestanden', '*.*')])
        if filename:
            try:
                if not os.path.exists(self.settings['error_log']):
                    with open(self.settings['error_log'], 'w', encoding='utf-8'
                              ):
                        pass
                with open(self.settings['error_log'], 'r', encoding='utf-8'
                          ) as src:
                    content = src.read()
                with open(filename, 'w', encoding='utf-8') as dst:
                    dst.write(content)
                messagebox.showinfo(
                    'Foutlog', f'Foutlog opgeslagen als {os.path.basename(filename)}')
            except Exception as e:
                messagebox.showerror('Fout', f'Fout bij opslaan: {e}')
                self.status_var.set(f'Fout bij opslaan: {e}')

    def open_settings(self):
        win = tk.Toplevel(self)
        win.title('Instellingen')
        win.geometry('420x500')
        tk.Label(win, text='Thema:').pack(anchor='w', padx=10, pady=(10, 0))
        theme_combo = ttk.Combobox(win, values=list(self.THEMES.keys()),
                                   textvariable=self.theme_var)
        theme_combo.pack(fill=tk.X, padx=10)
        tk.Label(win, text='Lettertype:').pack(anchor='w', padx=10, pady=(
            10, 0))
        import tkinter.font as tkfont
        font_choices = sorted(set(['Segoe UI',
                                   'Arial',
                                   'Calibri',
                                   'Consolas',
                                   'Courier New',
                                   'Comic Sans MS',
                                   'Verdana',
                                   'Tahoma',
                                   'Times New Roman',
                                   'Lucida Console',
                                   'Helvetica',
                                   'Georgia',
                                   'Impact',
                                   'Trebuchet MS',
                                   'Palatino Linotype',
                                   'Book Antiqua'] + list(tkfont.families())))
        font_entry = ttk.Combobox(
            win,
            values=font_choices,
            textvariable=self.font_family)
        font_entry.pack(fill=tk.X, padx=10)
        tk.Label(
            win,
            text='Lettergrootte:').pack(
            anchor='w',
            padx=10,
            pady=(
                10,
                0))
        font_size_entry = tk.Entry(win, textvariable=self.font_size)
        font_size_entry.pack(fill=tk.X, padx=10)
        tk.Label(win, text='Tekststijl:').pack(anchor='w', padx=10, pady=(
            10, 0))
        style_combo = ttk.Combobox(
            win,
            values=[
                'normaal',
                'vet',
                'cursief',
                'vet cursief',
                'onderstreept',
                'vet onderstreept',
                'cursief onderstreept',
                'vet cursief onderstreept'],
            textvariable=self.text_style)
        style_combo.pack(fill=tk.X, padx=10)
        tk.Label(
            win,
            text='Doeltaal (standaard):').pack(
            anchor='w',
            padx=10,
            pady=(
                10,
                0))
        target_combo = ttk.Combobox(
            win,
            values=[
                'Nederlands',
                'Engels',
                'Duits',
                'Frans',
                'Spaans',
                'Italiaans',
                'Portugees',
                'Pools',
                'Russisch',
                'Japans',
                'Chinees'],
            textvariable=self.target_lang_var)
        target_combo.pack(fill=tk.X, padx=10)

        def save_and_close():
            self.settings['theme'] = self.theme_var.get()
            self.settings['font_family'] = self.font_family.get()
            self.settings['font_size'] = self.font_size.get()
            self.settings['text_style'] = self.text_style.get()
            self.settings['target_language'] = self.target_lang_var.get()
            save_settings(self.settings)
            self.apply_theme()
            self.update_fonts()
            self.status_var.set('Instellingen opgeslagen.')
            win.destroy()
        ttk.Button(
            win,
            text='Opslaan',
            style='Blue.TButton',
            command=save_and_close).pack(
            pady=16)
        ttk.Button(win, text='Annuleren', command=win.destroy).pack()

    def reset_settings(self):
        save_settings(DEFAULT_SETTINGS)
        self.settings = load_settings()
        save_filters_config(DEFAULT_FILTER_CONFIG)
        self.filters_config = load_filters_config()
        self.font_family.set(self.settings['font_family'])
        self.font_size.set(self.settings['font_size'])
        self.text_style.set(self.settings['text_style'])
        self.theme_var.set(self.settings['theme'])
        self.target_lang_var.set(self.settings['target_language'])
        self.apply_theme()
        self.refresh_model_list()
        self.populate_lists_ui()
        self.status_var.set(
            'Instellingen zijn teruggezet naar standaardwaarden.')


APPNAME = 'SubtitleTranslatorPRO'
APPAUTHOR = 'MyCompany'
appdata_dir = appdirs.user_data_dir(APPNAME, APPAUTHOR, roaming=True)
os.makedirs(appdata_dir, exist_ok=True)
CONFIG_DIR = os.path.join(appdata_dir, 'config')
os.makedirs(CONFIG_DIR, exist_ok=True)
MODELS_DIR_DEFAULT = os.path.join(appdata_dir, 'models')
os.makedirs(MODELS_DIR_DEFAULT, exist_ok=True)
SCRIPT_EXPORT_DIR_DEFAULT = os.path.join(appdata_dir, 'script_export')
os.makedirs(SCRIPT_EXPORT_DIR_DEFAULT, exist_ok=True)
ERROR_LOG_FILE = os.path.join(appdata_dir, 'error.log')
LIST_CONVERTER_EXPORT_DIR = os.path.join(appdata_dir, 'list_converter_export')
os.makedirs(LIST_CONVERTER_EXPORT_DIR, exist_ok=True)
EXTERNAL_MODEL_DIR_FILE = os.path.join(appdata_dir, 'external_model_dir.txt')


def log_error(msg, settings_dict):
    try:
        if not os.path.exists(settings_dict.get('error_log', ERROR_LOG_FILE)):
            with open(settings_dict.get('error_log', ERROR_LOG_FILE), 'w',
                      encoding='utf-8'):
                pass
        with open(settings_dict.get('error_log', ERROR_LOG_FILE), 'a',
                  encoding='utf-8') as f:
            f.write(msg + '\n')
    except BaseException:
        pass


def clear_error_log(settings_dict):
    try:
        if os.path.exists(settings_dict.get('error_log', ERROR_LOG_FILE)):
            with open(settings_dict.get('error_log', ERROR_LOG_FILE), 'w',
                      encoding='utf-8'):
                pass
    except BaseException:
        pass


DEFAULT_SETTINGS = {
    'theme': 'neo_dark',
    'font_family': 'Segoe UI',
    'font_size': 12,
    'text_style': 'normaal',
    'timeout': 30,
    'target_language': 'Nederlands',
    'servers': {
        'ollama': {
            'key': '',
            'url': 'http://127.0.0.1',
            'port': 11434,
            'active': True,
            'timeout': 30,
            'gpu_support': {
                'enabled': True,
                'num_gpu_layers': 100,
                'gpu_memory': 'auto',
                'gpu_batch_size': 512}},
        'deepl': {
            'key': '',
            'active': True,
            'timeout': 30},
        'hugo': {
            'url': 'http://127.0.0.1',
            'port': 5678,
            'active': True,
            'timeout': 30}},
    'models': [
        'llama3:8b',
        'mistral:8x7b',
        'llama2:7b'],
    'active_model': 'llama3:8b',
    'external_model_dir': '',
    'error_log': ERROR_LOG_FILE,
    'spelling_language': 'Automatisch',
    'models_dir': MODELS_DIR_DEFAULT,
    'script_export_dir': SCRIPT_EXPORT_DIR_DEFAULT,
    'script_download_if_exe': True}
SETTINGS_FILE = os.path.join(CONFIG_DIR, 'settings.json')


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        s = DEFAULT_SETTINGS.copy()
        with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
            json.dump(s, f, indent=2, ensure_ascii=False)
        return s
    with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
        try:
            s = json.load(f)
        except BaseException:
            s = DEFAULT_SETTINGS.copy()
            with open(SETTINGS_FILE, 'w', encoding='utf-8') as fw:
                json.dump(s, fw, indent=2, ensure_ascii=False)
            return s
    for k, v in DEFAULT_SETTINGS.items():
        if k not in s:
            s[k] = v
        elif isinstance(v, dict) and isinstance(s[k], dict):
            for sk, sv in v.items():
                if sk not in s[k]:
                    s[k][sk] = sv
                if isinstance(sv, dict) and isinstance(s[k][sk], dict):
                    for ssk, ssv in sv.items():
                        if ssk not in s[k][sk]:
                            s[k][sk][ssk] = ssv
    return s


def save_settings(settings):
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=2, ensure_ascii=False)


FILTERS_CONFIG_FILE = os.path.join(CONFIG_DIR, 'filters_config.json')
ZINNEN_DICT = {'Do not allow them to sound the alarm.':
               'Laat ze niet toe om het alarm af te laten gaan'}
MILITARY_TERMS_DICT = {
    'AAA': 'Anti-Aircraft Artillery',
    'AAW': 'Anti-Air Warfare',
    'ABM': 'Anti-Ballistic Missile',
    'AFV': 'Armored Fighting Vehicle',
    'AWACS': 'Airborne Warning and Control System'}
SPECIALE_WOORDEN_DICT = {'Fuck': 'fuck', 'Yes': 'Ja', 'No': 'Nee', 'Copy':
                         'begrepen'}
USER_CUSTOM_DICT = {'Amsterdam': 'Amsterdam', 'Nederland': 'Nederland',
                    'Nederlands': 'Nederlands', 'Phoenix': 'Phoenix'}
DEFAULT_FILTER_CONFIG = {'filters_enabled': True,
                         'lists': [{'name': 'Zinnen Lijst',
                                    'enabled': True,
                                    'file_format': 'json',
                                    'source_url': '',
                                    'priority': 1,
                                    'items': ZINNEN_DICT},
                                   {'name': 'Speciale Woorden',
                                    'enabled': True,
                                    'file_format': 'json',
                                    'source_url': '',
                                    'priority': 2,
                                    'items': SPECIALE_WOORDEN_DICT},
                                   {'name': 'Military Terms',
                                    'enabled': True,
                                    'file_format': 'json',
                                    'source_url': '',
                                    'priority': 3,
                                    'items': MILITARY_TERMS_DICT},
                                   {'name': 'Eigen Aanpassingen',
                                    'enabled': True,
                                    'file_format': 'json',
                                    'source_url': '',
                                    'priority': 4,
                                    'items': USER_CUSTOM_DICT}]}


def load_filters_config():
    if not os.path.exists(FILTERS_CONFIG_FILE):
        with open(FILTERS_CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_FILTER_CONFIG, f, indent=2, ensure_ascii=False)
        return DEFAULT_FILTER_CONFIG
    with open(FILTERS_CONFIG_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except BaseException:
            data = DEFAULT_FILTER_CONFIG.copy()
            with open(FILTERS_CONFIG_FILE, 'w', encoding='utf-8') as fw:
                json.dump(data, fw, indent=2, ensure_ascii=False)
            return data
    for lst in data.get('lists', []):
        if 'priority' not in lst:
            lst['priority'] = 5
    return data


def save_filters_config(config):
    with open(FILTERS_CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def srt_time(ms):
    h, ms = divmod(ms, 3600000)
    m, s = divmod(ms, 60000)
    s, ms = divmod(s, 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'


def fully_clean_subtitle_line(txt):
    txt = re.sub(r'\\[.*?\\]', '', txt)
    txt = re.sub(r'\\(.*?\\)', '', txt)
    txt = re.sub(r'\\{.*?\\}', '', txt)
    txt = re.sub(r'\\<.*?\\>', '', txt)
    txt = re.sub(r'\\s+', ' ', txt).strip()
    return txt


def apply_filter_lists(txt, filter_config):
    if not filter_config.get('filters_enabled', True):
        return txt
    lists_data = filter_config.get('lists', [])
    lists_data = sorted(lists_data, key=lambda x: x.get('priority', 999))
    new_txt = txt
    for list_entry in lists_data:
        if list_entry.get('enabled', False):
            items_dict = list_entry.get('items', {})
            for old_word, new_word in items_dict.items():
                new_word_escaped = new_word.replace('\\', '\\\\')
                if ' ' in old_word.strip():
                    pattern = re.compile(re.escape(old_word), re.IGNORECASE)
                    new_txt = re.sub(pattern, new_word_escaped, new_txt)
                else:
                    pattern = '(?i)\\b' + re.escape(old_word) + '\\b'
                    new_txt = re.sub(pattern, new_word_escaped, new_txt)
    return new_txt


LANG_TOOL_MAP = {
    'Nederlands': 'nl-NL',
    'Engels': 'en-US',
    'Duits': 'de-DE',
    'Frans': 'fr-FR',
    'Spaans': 'es-ES',
    'Italiaans': 'it-IT',
    'Portugees': 'pt-PT',
    'Pools': 'pl-PL',
    'Russisch': 'ru-RU',
    'Japans': 'ja-JP',
    'Chinees': 'zh-CN'}
LANGUAGE_PROMPT_MAP = {
    'Nederlands': 'Dutch',
    'Engels': 'English',
    'Duits': 'German',
    'Frans': 'French',
    'Spaans': 'Spanish',
    'Italiaans': 'Italian',
    'Portugees': 'Portuguese',
    'Pools': 'Polish',
    'Russisch': 'Russian',
    'Japans': 'Japanese',
    'Chinees': 'Chinese'}
LANGDETECT_CODE_MAP = {
    'nl': 'Nederlands',
    'en': 'Engels',
    'de': 'Duits',
    'fr': 'Frans',
    'es': 'Spaans',
    'it': 'Italiaans',
    'pt': 'Portugees',
    'pl': 'Pools',
    'ru': 'Russisch',
    'ja': 'Japans',
    'zh': 'Chinees'}


def map_detected_language_code(detected_code):
    if not detected_code:
        return 'Engels'
    code_lower = detected_code.lower()
    for c in LANGDETECT_CODE_MAP:
        if code_lower.startswith(c):
            return LANGDETECT_CODE_MAP[c]
    return 'Engels'


try:
    import fasttext
    _fasttext_available = True
except ImportError:
    _fasttext_available = False
_fasttext_model = None


def load_fasttext_model():
    global _fasttext_model
    if not _fasttext_model and _fasttext_available:
        FASTTEXT_MODEL_PATH = os.path.join(appdata_dir, 'lid.176.bin')
        if os.path.exists(FASTTEXT_MODEL_PATH):
            _fasttext_model = fasttext.load_model(FASTTEXT_MODEL_PATH)


def detect_language_fasttext(txt):
    if not _fasttext_available:
        return None
    load_fasttext_model()
    if not _fasttext_model:
        return None
    prediction = _fasttext_model.predict(txt.replace('\n', ' '), k=1)
    if prediction and prediction[0]:
        label = prediction[0][0]
        if label.startswith('__label__'):
            return label.replace('__label__', '').strip()
    return None


def detect_language_fallback(txt):
    if not txt.strip():
        return 'en'
    code_ft = detect_language_fasttext(txt)
    if code_ft:
        return code_ft
    try:
        possible_langs = detect_langs(txt)
        if possible_langs:
            best_match = max(possible_langs, key=lambda l: l.prob)
            if best_match.prob < 0.5:
                return 'en'
            return best_match.lang
    except BaseException:
        pass
    return 'en'


def correct_spelling(txt, target_lang_name, tool_settings, parent_instance=None
                     ):
    """
    Corrigeer spelling. Als SpellChecker (pyspellchecker) voor Engels niet werkt
    (bijv. omdat de resource niet gevonden wordt),
    val dan terug op LanguageTool-python, zodat er geen error ontstaat.
    """
    tool_lang = LANG_TOOL_MAP.get(target_lang_name, 'en-US')
    try:
        if tool_lang.lower().startswith('en-'):
            if parent_instance and hasattr(
                    parent_instance,
                    'spellchecker') and parent_instance.spellchecker is not None:
                local_spellchecker = parent_instance.spellchecker
                words = txt.split()
                corrected_words = []
                for word in words:
                    if not word.isdigit() and word.isalpha() and (
                            word. islower() or word.istitle()):
                        c = local_spellchecker.correction(word)
                        corrected_words.append(c)
                    else:
                        corrected_words.append(word)
                return ' '.join(corrected_words)
            else:
                from language_tool_python import utils
                tool = language_tool_python.LanguageToolPublicAPI(tool_lang)
                matches = tool.check(txt)
                return utils.correct(txt, matches)
        else:
            from language_tool_python import utils
            tool = language_tool_python.LanguageToolPublicAPI(tool_lang)
            matches = tool.check(txt)
            return utils.correct(txt, matches)
    except Exception as e:
        log_error(f'Spelling correction error: {e}', tool_settings)
        return txt


def stop_all_model_servers(settings):
    for srv in settings['servers']:
        if settings['servers'][srv]['active']:
            try:
                if sys.platform == 'win32':
                    subprocess.run(f'taskkill /IM "{srv}.exe" /F', shell=True)
                else:
                    subprocess.run(f'pkill -f {srv}', shell=True)
            except Exception as e:
                log_error(f'{srv} stop error: {e}', settings)
    messagebox.showinfo('Noodstop', 'Alle actieve modelservers zijn gestopt.')


def remove_ai_disclaimers(text):
    patterns = [
        '(?i)\\bNeete:\\b.*',
        '(?i)\\bIn Dutch(s?)\\b.*',
        '(?i)\\bIf you want a more.*',
        '(?i)\\bThis translation aims.*',
        '(?i)\\bPlease provide .*',
        '(?i)\\bHoever\\b.*',
        '(?i)\\bdisclaimer.*',
        '(?i)\\bThis text is meant.*',
        '(?i)\\bAi Mori.*',
        '(?i)\\bLet me kNeew.*',
        '(?i)\\bCorrecting the translation to proper Dutch:.*',
        '(?i)\\bTheres more text to vertalen.*',
        '(?i)\\bmight affect.*',
        '(?i)\\bthe original text.*',
        '(?i)\\bthe naturalis.*',
        '(?i)\\bI am an AI model.*',
        '(?i)\\bI am ChatGPT.*',
        '(?i)\\bOpenAI is not responsible.*',
        '(?i)\\bAs ChatGPT.*',
        '(?i)\\bAs a large language model.*',
        '(?i)\\bAs an AI language model.*',
        '(?i)\\bAs an AI, I cannot.*',
        '(?i)\\bAs a responsible AI language model.*',
        '(?i)\\bI apologize.*',
        '(?i)\\bI canNeet provide.*',
        '(?i)\\bharmful and toxic language.*',
        '(?i)\\boffensive or harmful.*',
        '(?i)\\bviolence or terrorism.*',
        '(?i)\\bit is important to always use language.*',
        '(?i)\\bPlease refrain from using such language.*',
        '(?i)\\bIs there anything else I can help you with\\?.*',
        '(?i)\\bHere.*((T|t)ranslatie|translation).*',
        '(?i)\\bThe translation of.*',
        '(?i)\\bHere is the translation.*',
        '(?i)\\bI will now translate.*',
        '(?i)\\bIn summary, the translation.*',
        '(?i)\\bNote:\\s?.*',
        "(?i)\\bI(\\s)?\\'?ve translated.*",
        '(?i)\\bI used The.*',
        '(?i)\\bWhich I.*',
        '(?i)\\bWich I.*',
        '(?i)\\bWould be happy to help.*']
    cleaned = text
    for pat in patterns:
        cleaned = re.sub(pat, '', cleaned)
    cleaned = re.sub(r'\\s+', ' ', cleaned).strip()
    return cleaned


def levenshtein_distance(a, b):
    if a == b:
        return 0
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    v0 = list(range(len(b) + 1))
    v1 = [0] * (len(b) + 1)
    for i in range(len(a)):
        v1[0] = i + 1
        for j in range(len(b)):
            cost = 0 if a[i] == b[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        v0, v1 = v1, v0
    return v0[len(b)]


def choose_best_translation(candidate_translations, filter_config,
                            target_lang_name, original_text):
    if not candidate_translations:
        return ''
    valid_candidates = [fully_clean_subtitle_line(t).strip() for t in
                        candidate_translations if t.strip()]
    if not valid_candidates:
        return ''
    freq_map = {}
    for t in valid_candidates:
        freq_map[t] = freq_map.get(t, 0) + 1
    best = max(freq_map, key=freq_map.get)
    max_freq = freq_map[best]
    same_freq = [x for x in valid_candidates if freq_map[x] == max_freq]
    if len(same_freq) > 1:
        best = max(
            same_freq,
            key=lambda x: levenshtein_distance(
                x,
                original_text))
    return best


def finalize_result(raw_text, target_lang_name, filter_config,
                    parent_instance=None):
    text_no_disclaimers = remove_ai_disclaimers(raw_text)
    text_no_disclaimers = fully_clean_subtitle_line(text_no_disclaimers)
    spelled = correct_spelling(
        text_no_disclaimers,
        target_lang_name,
        parent_instance.settings if parent_instance else {},
        parent_instance)
    filtered = apply_filter_lists(spelled, filter_config)
    filtered = re.sub(r'\\s+', ' ', filtered).strip()
    return filtered


def export_subs(subs, filename):
    ext = os.path.splitext(filename)[1].lower()
    try:
        if ext == '.srt':
            subs.save(filename, format_='srt')
        elif ext == '.ass':
            subs.save(filename, format_='ass')
        elif ext == '.vtt':
            subs.save(filename, format_='vtt')
        elif ext == '.sub':
            subs.save(filename, format_='microdvd')
        else:
            subs.save(filename, format_='srt')
        return True, ''
    except Exception as e:
        return False, str(e)


def translate_with_server(
        server_name,
        text,
        source_lang_english,
        target_lang_name,
        settings,
        filter_config,
        model_file=None):
    target_english = LANGUAGE_PROMPT_MAP.get(target_lang_name, 'English')
    srv_cfg = settings['servers'].get(server_name, {})
    if not srv_cfg.get('active', False):
        return ''
    preprocessed_text = text
    if not preprocessed_text.strip():
        preprocessed_text = text
    try:
        if server_name == 'ollama':
            url = f"{srv_cfg['url']}:{srv_cfg['port']}/api/generate"
            prompt = f"""Please translate the following text from {source_lang_english} to {target_english} in a strictly natural way, without disclaimers or extra commentary:

{preprocessed_text}

Translated text:"""
            gpu_cfg = srv_cfg.get('gpu_support', {})
            gpu_enabled = gpu_cfg.get('enabled', False)
            extra_ollama_params = {}
            if gpu_enabled:
                num_gpu_layers = gpu_cfg.get('num_gpu_layers', 0)
                extra_ollama_params['num_gpu_layers'] = num_gpu_layers
                if gpu_cfg.get('gpu_memory'):
                    extra_ollama_params['gpu_memory'] = gpu_cfg['gpu_memory']
                if gpu_cfg.get('gpu_batch_size'):
                    extra_ollama_params['gpu_batch_size'] = gpu_cfg[
                        'gpu_batch_size']
            payload = {'model': settings.get('active_model', 'llama3:8b'),
                       'prompt': prompt, 'stream': False}
            if gpu_enabled:
                payload.update(extra_ollama_params)
            headers = {}
            ollama_key = srv_cfg.get('key', '')
            if ollama_key:
                headers['Authorization'] = f'Bearer {ollama_key}'
            resp = requests.post(url, json=payload, timeout=srv_cfg[
                'timeout'], headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                return data.get('response', text).strip()
        elif server_name == 'deepl':
            key = srv_cfg.get('key', '')
            if key:
                base_url = 'https://api-free.deepl.com/v2/translate'
                lang_map = {
                    'Nederlands': 'NL',
                    'Engels': 'EN',
                    'Duits': 'DE',
                    'Frans': 'FR',
                    'Spaans': 'ES',
                    'Italiaans': 'IT',
                    'Portugees': 'PT',
                    'Pools': 'PL',
                    'Russisch': 'RU',
                    'Japans': 'JA',
                    'Chinees': 'ZH'}
                target_code = lang_map.get(target_lang_name, 'EN')
                resp = requests.post(
                    base_url,
                    data={
                        'auth_key': key,
                        'text': preprocessed_text,
                        'target_lang': target_code},
                    timeout=srv_cfg['timeout'])
                if resp.status_code == 200:
                    data = resp.json()
                    if 'translations' in data and len(data['translations']
                                                      ) > 0:
                        return data['translations'][0]['text'].strip()
        elif server_name == 'hugo':
            url = f"{srv_cfg['url']}:{srv_cfg['port']}/translate"
            payload = {'text': preprocessed_text, 'source_language':
                       source_lang_english, 'target_language': target_english}
            resp = requests.post(url, json=payload, timeout=srv_cfg['timeout'])
            if resp.status_code == 200:
                data = resp.json()
                return data.get('translation', '').strip()
    except Exception as e:
        log_error(str(e), settings)
    return ''


class SubtitleTranslatorPro(tk.Tk):
    pass

    def __init__(self):
        super().__init__()
        self.settings = load_settings()
        self.filters_config = load_filters_config()
        self.spellchecker = None
        if SpellChecker:
            try:
                spellchecker = SpellChecker(language='en', distance=1)
            except Exception as e:
                log_error(f'Kon SpellChecker niet laden: {e}', self.settings)
                self.spellchecker = None
        self.title('Ondertitel Vertaler Pro - Compleet')
        self.geometry('1440x960')
        self.minsize(1000, 650)
        self.translating = threading.Event()
        self.spellcheck_stop_event = threading.Event()
        self.spellcheck_in_progress = threading.Event()
        self.auto_detect_enabled = True
        self.current_subs = None
        self.detected_language = None
        self.download_threads = {}
        self.status_var = tk.StringVar(value='Klaar')
        self.translated_subs = None
        self.spellchecked_subs = None
        self.font_family = tk.StringVar(value=self.settings.get(
            'font_family', 'Segoe UI'))
        self.font_size = tk.IntVar(value=self.settings.get('font_size', 12))
        self.text_style = tk.StringVar(value=self.settings.get('text_style',
                                                               'normaal'))
        self.theme_var = tk.StringVar(value=self.settings.get('theme',
                                                              'neo_dark'))
        self.target_lang_var = tk.StringVar(value=self.settings.get(
            'target_language', 'Nederlands'))
        self.source_lang_var = tk.StringVar(value='Automatisch')
        self.server_status_vars = {srv: tk.StringVar(value='Onbekend') for
                                   srv in self.settings['servers']}
        self.auto_scroll_enabled = True
        self.create_styles()
        self.create_widgets()
        self.apply_theme()
        self.theme_var.trace_add('write', self.change_theme_immediately)
        self.after(1000, self.periodic_server_status)

    def create_styles(self):
        THEMES = {
            'modern_black': {
                'bg': '#0a0a0a',
                'fg': '#ffffff',
                'accent': '#2563eb',
                'tab': '#1a1a1a',
                'entry_bg': '#181818',
                'entry_fg': '#ffffff',
                'button_fg': '#ffffff',
                'button_bg': '#2563eb',
                'button_active': '#174ea6',
                'red': '#e11d48',
                'blue': '#2563eb',
                'green': '#22c55e',
                'border': '#ffffff'},
            'modern_blue': {
                'bg': '#1e3a8a',
                'fg': '#ffffff',
                'accent': '#60a5fa',
                'tab': '#1e40af',
                'entry_bg': '#1e40af',
                'entry_fg': '#ffffff',
                'button_fg': '#ffffff',
                'button_bg': '#3b82f6',
                'button_active': '#2563eb',
                'red': '#ef4444',
                'blue': '#3b82f6',
                'green': '#06d6a0',
                'border': '#ffffff'},
            'neo_dark': {
                'bg': '#000000',
                'fg': '#39FF14',
                'accent': '#00FFFF',
                'tab': '#222222',
                'entry_bg': '#111111',
                'entry_fg': '#39FF14',
                'button_fg': '#000000',
                'button_bg': '#39FF14',
                'button_active': '#00FF7F',
                'red': '#FF0080',
                'blue': '#00FFFF',
                'green': '#00ff00',
                'border': '#39FF14'}}
        self.THEMES = THEMES
        self.THEMES.update(extra_neo_themes())
        style = ttk.Style(self)
        style.theme_use('clam')
        theme = THEMES.get(self.theme_var.get(), THEMES['neo_dark'])
        style.configure(
            'Blue.TButton',
            background=theme['button_bg'],
            foreground=theme['button_fg'],
            font=(
                'Segoe UI',
                10,
                'bold'),
            padding=4)
        style.map('Blue.TButton', background=[('active', theme[
            'button_active']), ('pressed', theme['button_active'])],
            foreground=[('active', theme['button_fg'])])
        style.configure(
            'Status.TLabel',
            background=theme['bg'],
            foreground=theme['fg'],
            font=(
                'Segoe UI',
                9))
        style.configure('blue.Horizontal.TProgressbar', troughcolor=theme[
            'bg'], bordercolor=theme['bg'], background=theme['accent'] if
            'accent' in theme else '#00FFFF', lightcolor=theme['accent'] if
            'accent' in theme else '#00FFFF', darkcolor=theme['accent'] if
            'accent' in theme else '#00FFFF')

    def change_theme_immediately(self, *args):
        self.settings['theme'] = self.theme_var.get()
        save_settings(self.settings)
        self.apply_theme()

    def get_font(self):
        style_map = {
            'normaal': (
                'normal', 'roman'), 'vet': (
                'bold', 'roman'), 'cursief': (
                'normal', 'italic'), 'vet cursief': (
                    'bold', 'italic'), 'onderstreept': (
                        'normal', 'roman', 'underline'), 'vet onderstreept': (
                            'bold', 'roman', 'underline'), 'cursief onderstreept': (
                                'normal', 'italic', 'underline'), 'vet cursief onderstreept': (
                                    'bold', 'italic', 'underline')}
        style = self.text_style.get()
        font_family = self.font_family.get() or 'Segoe UI'
        font_size = self.font_size.get() or 12
        style_tuple = style_map.get(style, ('normal', 'roman'))
        weight = style_tuple[0] if len(style_tuple) > 0 else 'normal'
        slant = style_tuple[1] if len(style_tuple) > 1 else 'roman'
        underline = False
        if len(style_tuple) > 2 and 'underline' in style_tuple[2:]:
            underline = True
        if slant not in ('roman', 'italic'):
            slant = 'roman'
        if weight not in ('normal', 'bold'):
            weight = 'normal'
        return font.Font(family=font_family, size=font_size, weight=weight,
                         slant=slant, underline=underline)

    def apply_theme(self):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        self.configure(bg=theme['bg'])

        def apply_bg_recursively(parent):
            for w in parent.winfo_children():
                try:
                    w.configure(bg=theme['bg'])
                except BaseException:
                    pass
                apply_bg_recursively(w)
        apply_bg_recursively(self)
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure(
            'Blue.TButton',
            background=theme['button_bg'],
            foreground=theme['button_fg'],
            font=(
                'Segoe UI',
                10,
                'bold'),
            padding=4)
        style.map('Blue.TButton', background=[('active', theme[
            'button_active']), ('pressed', theme['button_active'])],
            foreground=[('active', theme['button_fg'])])
        style.configure(
            'Status.TLabel',
            background=theme['bg'],
            foreground=theme['fg'],
            font=(
                'Segoe UI',
                9))
        style.configure('blue.Horizontal.TProgressbar', troughcolor=theme[
            'bg'], bordercolor=theme['bg'], background=theme['accent'] if
            'accent' in theme else '#00FFFF', lightcolor=theme['accent'] if
            'accent' in theme else '#00FFFF', darkcolor=theme['accent'] if
            'accent' in theme else '#00FFFF')
        self.update_idletasks()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        self.tab_translate = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_translate, text='Vertalen')
        self.create_translation_tab(self.tab_translate)
        self.tab_models = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_models, text='Modelbeheer')
        self.create_model_tab(self.tab_models)
        self.tab_servers = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_servers, text='Serverbeheer')
        self.create_server_tab(self.tab_servers)
        self.tab_info = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_info, text='Info')
        self.create_info_tab(self.tab_info)
        self.tab_filters = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_filters, text='Filters en lijsten')
        self.create_filters_and_lists_tab(self.tab_filters)
        self.tab_lijst_convertor = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_lijst_convertor, text='Lijst Convertor')
        self.create_list_converter_tab(self.tab_lijst_convertor)
        self.tab_spellcheck = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_spellcheck, text='Spellingcontrole')
        self.create_spellcheck_tab(self.tab_spellcheck)
        menubar = tk.Menu(self)
        bestand_menu = tk.Menu(menubar, tearoff=0)
        bestand_menu.add_command(label='Open ondertitel...', command=self.
                                 open_subtitle)
        bestand_menu.add_command(label='Opslaan als...', command=self.
                                 save_subtitle)
        bestand_menu.add_separator()
        bestand_menu.add_command(label='Script downloaden', command=self.
                                 download_script)
        bestand_menu.add_command(label='Foutlog wissen', command=lambda:
                                 clear_error_log(self.settings))
        bestand_menu.add_command(
            label='Foutlog opslaan als...',
            command=self.save_error_log)
        bestand_menu.add_separator()
        bestand_menu.add_command(label='Afsluiten', command=self.quit)
        menubar.add_cascade(label='Bestand', menu=bestand_menu)
        opties_menu = tk.Menu(menubar, tearoff=0)
        opties_menu.add_command(label='Instellingen', command=self.
                                open_settings)
        opties_menu.add_command(label='Reset instellingen', command=self.
                                reset_settings)
        menubar.add_cascade(label='Opties', menu=opties_menu)
        self.config(menu=menubar)
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        statusbar = tk.Frame(self, height=24, bg=theme['bg'])
        statusbar.pack(fill=tk.X, side=tk.BOTTOM)
        self.status_label = ttk.Label(
            statusbar,
            textvariable=self. status_var,
            style='Status.TLabel',
            anchor='w')
        self.status_label.pack(side=tk.LEFT, padx=8)

    def periodic_server_status(self):
        self.check_server_status()
        self.after(5000, self.periodic_server_status)

    def create_translation_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.Frame(parent, bg=theme['bg'], highlightbackground=theme[
            'border'], highlightthickness=4)
        frame.pack(fill=tk.BOTH, expand=True)
        topbar = tk.Frame(frame, bg=theme['bg'])
        topbar.pack(fill=tk.X, pady=(8, 8))
        ttk.Button(
            topbar,
            text='Vertalen starten',
            style='Blue.TButton',
            command=self.live_translate).pack(
            side=tk.LEFT,
            padx=6,
            ipadx=8,
            ipady=2)
        ttk.Button(
            topbar,
            text='Stop vertalen',
            style='Blue.TButton',
            command=self.stop_translate).pack(
            side=tk.LEFT,
            padx=6,
            ipadx=8,
            ipady=2)
        ttk.Button(topbar, text='Vertaling wissen', style='Blue.TButton',
                   command=self.clear_translation).pack(side=tk.LEFT, padx=6,
                                                        ipadx=8, ipady=2)
        self.auto_scroll_btn = ttk.Button(
            topbar,
            text='Auto-scroll: Aan',
            style='Blue.TButton',
            command=self.toggle_auto_scroll)
        self.auto_scroll_btn.pack(side=tk.LEFT, padx=6, ipadx=8, ipady=2)
        self.auto_detect_btn = ttk.Button(
            topbar,
            text='Autom. taalherkenning: Aan',
            style='Blue.TButton',
            command=self.toggle_auto_detect)
        self.auto_detect_btn.pack(side=tk.LEFT, padx=6, ipadx=8, ipady=2)
        left = tk.Frame(frame, bg=theme['bg'], highlightbackground=theme[
            'blue'], highlightthickness=2)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(left, text='Origineel', font=self.get_font(), bg=theme[
            'bg'], fg=theme['fg']).pack(anchor='w')
        orig_scroll = tk.Scrollbar(left)
        orig_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_original = tk.Text(
            left,
            width=50,
            height=30,
            font=self. get_font(),
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['entry_fg'],
            highlightbackground=theme['border'],
            highlightthickness=2,
            yscrollcommand=orig_scroll.set)
        self.text_original.pack(fill=tk.BOTH, expand=True, pady=2)
        orig_scroll.config(command=self.text_original.yview)
        right = tk.Frame(frame, bg=theme['bg'], highlightbackground=theme[
            'red'], highlightthickness=2)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(right, text='Vertaling', font=self.get_font(), bg=theme[
            'bg'], fg=theme['fg']).pack(anchor='w')
        trans_scroll = tk.Scrollbar(right)
        trans_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_translation = tk.Text(
            right,
            width=50,
            height=30,
            font=self.get_font(),
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['entry_fg'],
            highlightbackground=theme['border'],
            highlightthickness=2,
            yscrollcommand=trans_scroll.set)
        self.text_translation.pack(fill=tk.BOTH, expand=True, pady=2)
        trans_scroll.config(command=self.text_translation.yview)
        bottom = tk.Frame(frame, bg=theme['bg'])
        bottom.pack(fill=tk.X, pady=4)
        tk.Label(bottom, text='Bron-taal:', bg=theme['bg'], fg=theme['fg']
                 ).pack(side=tk.LEFT, padx=4)
        LANGUAGES = ['Automatisch', 'Nederlands', 'Engels', 'Duits',
                     'Frans', 'Spaans', 'Italiaans', 'Portugees', 'Pools',
                     'Russisch', 'Japans', 'Chinees']
        self.source_lang_combo = ttk.Combobox(
            bottom, values=LANGUAGES, textvariable=self.source_lang_var, width=16)
        self.source_lang_combo.pack(side=tk.LEFT, padx=4)
        tk.Label(bottom, text='Doeltaal:', bg=theme['bg'], fg=theme['fg']
                 ).pack(side=tk.LEFT, padx=(16, 4))
        target_languages = [
            'Nederlands',
            'Engels',
            'Duits',
            'Frans',
            'Spaans',
            'Italiaans',
            'Portugees',
            'Pools',
            'Russisch',
            'Japans',
            'Chinees']
        self.target_lang_combo = ttk.Combobox(
            bottom,
            values=target_languages,
            textvariable=self.target_lang_var,
            width=16)
        self.target_lang_combo.pack(side=tk.LEFT, padx=4)
        self.detect_once_button = ttk.Button(
            bottom,
            text='Detecteer bron-taal eenmalig',
            style='Blue.TButton',
            command=self.user_triggered_detect_language)
        self.detect_once_button.pack(side=tk.LEFT, padx=4, ipadx=4)
        self.text_original.bind('<KeyRelease>', self.maybe_auto_detect_language
                                )
        tk.Label(bottom, text='Tekststijl:', bg=theme['bg'], fg=theme['fg']
                 ).pack(side=tk.LEFT, padx=8)
        self.text_style_combo = ttk.Combobox(
            bottom,
            values=[
                'normaal',
                'vet',
                'cursief',
                'vet cursief',
                'onderstreept',
                'vet onderstreept',
                'cursief onderstreept',
                'vet cursief onderstreept'],
            textvariable=self.text_style,
            width=18)
        self.text_style_combo.pack(side=tk.LEFT, padx=4)
        self.text_style_combo.bind('<<ComboboxSelected>>', lambda e: self.
                                   update_fonts())
        tk.Label(bottom, text='Lettergrootte:', bg=theme['bg'], fg=theme['fg']
                 ).pack(side=tk.LEFT, padx=8)
        self.font_size_spin = tk.Spinbox(
            bottom,
            from_=8,
            to=48,
            textvariable=self.font_size,
            width=4,
            command=self.update_fonts)
        self.font_size_spin.pack(side=tk.LEFT, padx=4)
        self.font_size.trace('w', lambda *a: self.update_fonts())
        self.font_family.trace('w', lambda *a: self.update_fonts())
        progress_frame = tk.Frame(frame, bg=theme['bg'])
        progress_frame.pack(fill=tk.X, pady=(0, 6))
        self.progress_var = tk.DoubleVar(value=0)
        self.progress_label = tk.Label(
            progress_frame,
            text='0/0 regels vertaald',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font())
        self.progress_label.pack(side=tk.LEFT, padx=8)
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            variable=self. progress_var,
            maximum=100,
            style='blue.Horizontal.TProgressbar')
        self.progress_bar.pack(fill=tk.X, expand=True, padx=8, side=tk.LEFT)

    def toggle_auto_scroll(self):
        self.auto_scroll_enabled = not self.auto_scroll_enabled
        self.auto_scroll_btn.config(
            text=f"Auto-scroll: {'Aan' if self.auto_scroll_enabled else 'Uit'}")
        self.status_var.set(
            f"Auto-scroll is {'ingeschakeld' if self.auto_scroll_enabled else 'uitgeschakeld'}."
        )

    def toggle_auto_detect(self):
        self.auto_detect_enabled = not self.auto_detect_enabled
        if self.auto_detect_enabled:
            self.auto_detect_btn.config(text='Autom. taalherkenning: Aan')
            self.status_var.set('Automatische taalherkenning is ingeschakeld.')
            self.auto_detect_language()
        else:
            self.auto_detect_btn.config(text='Autom. taalherkenning: Uit')
            self.status_var.set('Automatische taalherkenning is uitgeschakeld.'
                                )

    def maybe_auto_detect_language(self, event=None):
        if self.auto_detect_enabled and self.source_lang_var.get(
        ) == 'Automatisch':
            txt = self.text_original.get('1.0', tk.END).strip()
            if len(txt) >= 30:
                self.auto_detect_language()

    def user_triggered_detect_language(self):
        if self.source_lang_var.get() != 'Automatisch':
            self.status_var.set("Bron-taal staat niet op 'Automatisch'.")
        else:
            self.auto_detect_language()

    def update_fonts(self, *args):
        f = self.get_font()
        self.text_original.configure(font=f)
        self.text_translation.configure(font=f)
        self.progress_label.configure(font=f)

    def auto_detect_language(self):
        text = self.text_original.get('1.0', tk.END).strip()
        if not text:
            self.status_var.set('Geen tekst om te detecteren.')
            return
        if len(text) < 30:
            self.status_var.set(
                'Tekst is te kort voor betrouwbare taalherkenning.')
            return
        try:
            code = detect_language_fallback(text)
            self.detected_language = code
            if self.detected_language:
                mapped_lang = map_detected_language_code(self.detected_language
                                                         )
                self.status_var.set(
                    f'Gedetecteerde taal: {mapped_lang} (code={code}).')
            else:
                self.status_var.set('Kon geen taal herkennen.')
        except LangDetectException:
            self.status_var.set('Taal niet herkend door langdetect.')

    def open_subtitle(self):
        filename = filedialog.askopenfilename(
            title='Open ondertitelbestand',
            filetypes=[
                ('Ondertiteling',
                 '*.srt *.vtt *.ass *.sub *.sbv *.stl *.ssa *.txt'),
                ('Alle bestanden',
                 '*.*')])
        if filename:
            try:
                subs = pysubs2.load(filename)
                self.current_subs = subs
                self.text_original.delete('1.0', tk.END)
                for i, line in enumerate(subs):
                    srt_line = f"""{i + 1}
{srt_time(line.start)} --> {srt_time(line.end)}
{line.text}

"""
                    self.text_original.insert(tk.END, srt_line)
                if self.auto_detect_enabled and self.source_lang_var.get(
                ) == 'Automatisch':
                    self.auto_detect_language()
                self.status_var.set(
                    f'Bestand geladen: {os.path.basename(filename)}')
            except Exception as e:
                messagebox.showerror('Fout', f'Fout bij laden: {e}')
                log_error(str(e), self.settings)
                self.status_var.set('Fout bij laden.')

    def save_subtitle(self):
        choice = messagebox.askyesno(
            'Opslaan',
            'Wil je het resultaat uit de Spellingcontrole-tab opslaan? (Ja = Spellingcontrole, Nee = Vertaling)')
        filename = filedialog.asksaveasfilename(
            title='Opslaan als',
            defaultextension='.srt',
            filetypes=[
                ('SubRip (.srt)',
                 '*.srt'),
                ('ASS (.ass)',
                 '*.ass'),
                ('WebVTT (.vtt)',
                 '*.vtt'),
                ('MicroDVD (.sub)',
                 '*.sub'),
                ('Alle bestanden',
                 '*.*')])
        if not filename:
            return
        if choice:
            if not self.spellchecked_subs or len(self.spellchecked_subs) == 0:
                messagebox.showwarning(
                    'Geen data', 'Er zijn geen spelling-gecorrigeerde subs om op te slaan.')
                return
            success, err = export_subs(self.spellchecked_subs, filename)
        else:
            if not self.translated_subs or len(self.translated_subs) == 0:
                messagebox.showwarning(
                    'Geen data', 'Er zijn geen vertaalde subs om op te slaan.')
                return
            success, err = export_subs(self.translated_subs, filename)
        if success:
            messagebox.showinfo(
                'Opgeslagen',
                f'Bestand succesvol opgeslagen als {os.path.basename(filename)}.')
            self.status_var.set(f'Opgeslagen als: {os.path.basename(filename)}'
                                )
        else:
            messagebox.showerror('Fout', f'Fout bij opslaan: {err}')
            self.status_var.set('Fout bij opslaan.')

    def live_translate(self):
        if not self.current_subs:
            messagebox.showwarning('Geen ondertitel',
                                   'Laad eerst een ondertitelbestand.')
            self.status_var.set('Geen ondertitel geladen.')
            return
        self.text_translation.delete('1.0', tk.END)
        target = self.target_lang_var.get()
        lines = list(self.current_subs)
        self.translating.set()
        total = len(lines)
        self.progress_var.set(0)
        self.progress_label.config(text=f'0/{total} regels vertaald')
        self.status_var.set(f'Vertalen gestart: 0/{total} regels.')
        self.translated_subs = pysubs2.SSAFile()
        if self.source_lang_var.get(
        ) == 'Automatisch' and not self.detected_language:
            combined_text = '\n'.join([l.text for l in lines])
            if len(combined_text) > 30:
                try:
                    code = detect_language_fallback(combined_text)
                    if code:
                        self.detected_language = code
                except BaseException:
                    pass
        if self.source_lang_var.get() != 'Automatisch':
            source_lang_name = self.source_lang_var.get()
            source_english = LANGUAGE_PROMPT_MAP.get(source_lang_name,
                                                     'English')
        elif self.detected_language:
            mapped = map_detected_language_code(self.detected_language)
            source_english = LANGUAGE_PROMPT_MAP.get(mapped, 'English')
        else:
            source_english = 'English'

        def do_translate():
            servers_list = list(self.settings['servers'].keys())
            for idx, line in enumerate(lines):
                if not self.translating.is_set():
                    self.status_var.set('Live vertalen gestopt.')
                    return
                text_line_preprocessed = apply_filter_lists(line.text, self
                                                            .filters_config)
                if not text_line_preprocessed.strip():
                    text_line_preprocessed = line.text
                candidate_trans = []
                for srv_name in servers_list:
                    res = translate_with_server(
                        srv_name,
                        text_line_preprocessed,
                        source_english,
                        target,
                        self.settings,
                        self.filters_config)
                    if res:
                        candidate_trans.append(res)
                if not candidate_trans:
                    final_translation_raw = text_line_preprocessed
                else:
                    final_translation_raw = choose_best_translation(
                        candidate_trans, self.filters_config, target,
                        text_line_preprocessed)
                    if not final_translation_raw.strip():
                        final_translation_raw = text_line_preprocessed
                final_translation = finalize_result(
                    final_translation_raw, target, self.filters_config, self)
                srt_line = f"""{idx + 1}
{srt_time(line.start)} --> {srt_time(line.end)}
{final_translation}

"""
                self.text_translation.insert(tk.END, srt_line)
                new_line = line.copy()
                new_line.text = final_translation
                self.translated_subs.append(new_line)
                self.status_var.set(f'Live: Regel {idx + 1}/{total} vertaald.')
                self.progress_var.set((idx + 1) / total * 100)
                self.progress_label.config(
                    text=f'{idx + 1}/{total} regels vertaald')
                self.update_idletasks()
                if self.auto_scroll_enabled:
                    self.text_translation.yview_moveto(1)
            self.status_var.set(
                f'Live vertaling voltooid: {total}/{total} regels.')
            self.translating.clear()
            messagebox.showinfo('Vertaling klaar', 'De vertaling is voltooid!')
        threading.Thread(target=do_translate, daemon=True).start()

    def stop_translate(self):
        self.translating.clear()
        self.status_var.set('Live vertalen gestopt.')
        messagebox.showinfo('Stop vertalen', 'Live vertalen gestopt.')

    def clear_translation(self):
        self.text_translation.delete('1.0', tk.END)
        self.translated_subs = None
        self.status_var.set('Vertaling gewist.')

    def create_model_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.Frame(parent, bg=theme['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        tk.Label(frame, text='Modelbeheer', font=self.get_font(), bg=theme[
            'bg'], fg=theme['fg']).pack(anchor='w', pady=2)
        self.model_listbox = tk.Listbox(
            frame,
            height=8,
            font=self.get_font(),
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            selectbackground=theme['accent'])
        self.model_listbox.pack(fill=tk.X, pady=2)
        self.refresh_model_list()
        btn_frame = tk.Frame(frame, bg=theme['bg'])
        btn_frame.pack(fill=tk.X, pady=6)

        def open_model_search():
            webbrowser.open_new('https://ollama.com/search')
            self.status_var.set(
                'Website https://ollama.com/search geopend in browser.')
        ttk.Button(
            btn_frame,
            text='Zoek modellen…',
            style='Blue.TButton',
            command=open_model_search).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Download + toevoegen (lokaal)',
            style='Blue.TButton',
            command=self.download_and_add_local).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Download + toevoegen (extern)',
            style='Blue.TButton',
            command=self.download_and_add_external).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Activeer model',
            style='Blue.TButton',
            command=self.activate_model_local).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Activeer model (extern)',
            style='Blue.TButton',
            command=self.activate_model_external).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Stop huidige model',
            style='Blue.TButton',
            command=self.stop_current_model).pack(
            side=tk. LEFT,
            padx=4,
            ipadx=4)
        ttk.Button(
            btn_frame,
            text='Verwijderen',
            style='Blue.TButton',
            command=self.remove_model).pack(
            side=tk.LEFT,
            padx=4,
            ipadx=4)
        ext_frame = tk.Frame(frame, bg=theme['bg'])
        ext_frame.pack(fill=tk.X, pady=(12, 2))
        tk.Label(
            ext_frame,
            text='Externe model-pad:',
            bg=theme['bg'],
            fg=theme['fg']).pack(
            side=tk.LEFT,
            padx=2)
        self.ext_model_dir_var = tk.StringVar(value=self.settings.get(
            'external_model_dir', ''))
        self.ext_model_entry = tk.Entry(
            ext_frame,
            textvariable=self. ext_model_dir_var,
            width=40,
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['entry_fg'])
        self.ext_model_entry.pack(side=tk.LEFT, padx=2)
        ttk.Button(
            ext_frame,
            text='Kies map',
            style='Blue.TButton',
            command=self.choose_external_directory).pack(
            side=tk.LEFT,
            padx=2)
        self.model_progress = tk.DoubleVar(value=0)
        self.model_progress_label = tk.Label(
            frame,
            text='Status: klaar',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font())
        self.model_progress_label.pack(fill=tk.X, padx=8, pady=(8, 2))
        self.progress_bar_models = ttk.Progressbar(frame, variable=self.
                                                   model_progress, maximum=100)
        self.progress_bar_models.pack(fill=tk.X, pady=4)

    def stop_current_model(self):
        stop_all_model_servers(self.settings)
        self.status_var.set('Huidige modelserver is gestopt.')

    def refresh_model_list(self):
        self.model_listbox.delete(0, tk.END)
        for m in self.settings.get('models', []):
            self.model_listbox.insert(tk.END, m)
        if self.settings.get('active_model') in self.settings.get('models', []
                                                                  ):
            idx = self.settings['models'].index(self.settings['active_model'])
            self.model_listbox.selection_set(idx)

    def choose_external_directory(self):
        directory = filedialog.askdirectory(
            title='Kies een map op je externe schijf voor modellen')
        if not directory:
            return
        try:
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
            modellen_subdir = os.path.join(directory, 'modellen')
            if not os.path.exists(modellen_subdir):
                os.makedirs(modellen_subdir, exist_ok=True)
            self.settings['external_model_dir'] = directory
            save_settings(self.settings)
            self.ext_model_dir_var.set(directory)
            messagebox.showinfo('Extern model-pad',
                                f'Extern model-pad ingesteld op:\n{directory}')
            self.status_var.set(f'Extern model-pad: {directory}')
        except Exception as e:
            messagebox.showerror('Fout', f'Fout bij instellen extern pad: {e}')
            log_error(str(e), self.settings)

    def download_and_add_local(self):
        model = simpledialog.askstring('Model toevoegen (lokaal)',
                                       'Voer de naam van het model in:')
        if not model:
            return
        messagebox.showinfo('Download gestart',
                            f"Download van '{model}' (lokaal) gestart.")
        self.model_progress.set(0)
        self.model_progress_label.config(
            text=f"Download gestart voor '{model}' (lokaal)...")
        self.status_var.set(f"Download gestart voor '{model}' (lokaal)...")

        def do_download_local():
            try:
                url = (
                    f"{self.settings['servers']['ollama']['url']}:{self.settings['servers']['ollama']['port']}/api/pull"
                )
                resp = requests.post(url, json={'name': model}, stream=True,
                                     timeout=600)
                if resp.status_code != 200:
                    raise Exception(f'Server gaf status {resp.status_code}')
                model_path = os.path.join(MODELS_DIR_DEFAULT, model + '.bin')
                with open(model_path, 'wb') as f:
                    chunk_count = 0
                    for chunk in resp.iter_content(chunk_size=8192):
                        if not chunk:
                            continue
                        f.write(chunk)
                        chunk_count += 1
                        if chunk_count % 50 == 0:
                            self.model_progress.set(
                                min(100, self. model_progress.get() + 3))
                            self.model_progress_label.config(
                                text=f"Download '{model}' (lokaal) ~{self.model_progress.get():.1f}%")
                            self.update_idletasks()
                if model not in self.settings['models']:
                    self.settings['models'].append(model)
                save_settings(self.settings)
                self.refresh_model_list()
                self.status_var.set(
                    f"Model '{model}' succesvol gedownload (lokaal).")
                self.model_progress_label.config(
                    text=f"Model '{model}' succesvol gedownload (lokaal).")
                messagebox.showinfo('Download voltooid',
                                    f"Model '{model}' is lokaal toegevoegd.")
            except Exception as e:
                self.status_var.set(f'Fout bij downloaden: {e}')
                self.model_progress_label.config(
                    text=f'Fout bij downloaden: {e}')
                log_error(str(e), self.settings)
                messagebox.showerror('Download', f'Fout bij downloaden: {e}')
            self.model_progress.set(0)
        t = threading.Thread(target=do_download_local, daemon=True)
        self.download_threads[model] = t
        t.start()

    def download_and_add_external(self):
        if not self.settings.get('external_model_dir'):
            messagebox.showwarning('Geen externe map',
                                   'Stel eerst het externe model-pad in.')
            return
        model = simpledialog.askstring('Model toevoegen (extern)',
                                       'Voer de naam van het model in:')
        if not model:
            return
        messagebox.showinfo('Download gestart',
                            f"Download van '{model}' (extern) gestart.")
        self.model_progress.set(0)
        self.model_progress_label.config(
            text=f"Download gestart voor '{model}' (extern)...")
        self.status_var.set(f"Download gestart voor '{model}' (extern)...")

        def do_download_external():
            try:
                url = (
                    f"{self.settings['servers']['ollama']['url']}:{self.settings['servers']['ollama']['port']}/api/pull"
                )
                resp = requests.post(url, json={'name': model}, stream=True,
                                     timeout=600)
                if resp.status_code != 200:
                    raise Exception(f'Server gaf status {resp.status_code}')
                ext_dir = os.path.join(self.settings['external_model_dir'],
                                       'modellen')
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir, exist_ok=True)
                model_path = os.path.join(ext_dir, model + '.bin')
                with open(model_path, 'wb') as f:
                    chunk_count = 0
                    for chunk in resp.iter_content(chunk_size=8192):
                        if not chunk:
                            continue
                        f.write(chunk)
                        chunk_count += 1
                        if chunk_count % 50 == 0:
                            self.model_progress.set(
                                min(100, self. model_progress.get() + 3))
                            self.model_progress_label.config(
                                text=f"Download '{model}' (extern) ~{self.model_progress.get():.1f}%")
                            self.update_idletasks()
                if model not in self.settings['models']:
                    self.settings['models'].append(model)
                save_settings(self.settings)
                self.refresh_model_list()
                self.status_var.set(
                    f"Model '{model}' succesvol gedownload (extern).")
                self.model_progress_label.config(
                    text=f"Model '{model}' succesvol gedownload (extern).")
                messagebox.showinfo('Download voltooid',
                                    f"Model '{model}' is extern toegevoegd.")
            except Exception as e:
                self.status_var.set(f'Fout bij downloaden: {e}')
                self.model_progress_label.config(
                    text=f'Fout bij downloaden: {e}')
                log_error(str(e), self.settings)
                messagebox.showerror('Download', f'Fout bij downloaden: {e}')
            self.model_progress.set(0)
        t = threading.Thread(target=do_download_external, daemon=True)
        self.download_threads[model] = t
        t.start()

    def activate_model_local(self):
        sel = self.model_listbox.curselection()
        if not sel:
            messagebox.showwarning(
                'Selecteer model',
                'Selecteer een model om lokaal te activeren.')
            return
        model = self.model_listbox.get(sel[0])
        self.model_progress_label.config(
            text=f"Model '{model}' activeren (lokaal)...")
        self.settings['active_model'] = model
        save_settings(self.settings)
        self.refresh_model_list()
        messagebox.showinfo('Activeren',
                            f"Model '{model}' is nu actief (lokaal).")
        self.status_var.set(f"Model '{model}' is nu actief (lokaal).")
        self.model_progress_label.config(
            text=f"Model '{model}' is nu actief (lokaal).")

    def activate_model_external(self):
        if not self.settings.get('external_model_dir'):
            messagebox.showwarning('Geen externe map',
                                   'Stel eerst een extern model-pad in.')
            return
        sel = self.model_listbox.curselection()
        if not sel:
            messagebox.showwarning(
                'Selecteer model',
                'Selecteer een model om extern te activeren.')
            return
        model = self.model_listbox.get(sel[0])
        ext_dir = os.path.join(self.settings['external_model_dir'], 'modellen')
        ext_file = os.path.join(ext_dir, model + '.bin')
        if not os.path.exists(ext_file):
            msg = f"""Het geselecteerde model '{model}' lijkt niet te bestaan in:
{ext_file}

We activeren het toch in de software, maar het bestand ontbreekt mogelijk."""
            messagebox.showwarning('Model extern niet gevonden', msg)
        self.settings['active_model'] = model
        save_settings(self.settings)
        self.refresh_model_list()
        messagebox.showinfo('Externe model activeren',
                            f"Model '{model}' is nu actief (extern).")
        self.status_var.set(f"Model '{model}' is nu actief (extern).")
        self.model_progress_label.config(text=f"Model '{model}' extern actief."
                                         )

    def remove_model(self):
        sel = self.model_listbox.curselection()
        if not sel:
            messagebox.showwarning('Selecteer model',
                                   'Selecteer een model om te verwijderen.')
            return
        model = self.model_listbox.get(sel[0])
        if model in self.settings['models']:
            self.settings['models'].remove(model)
        if self.settings.get('active_model') == model:
            self.settings['active_model'] = ''
        save_settings(self.settings)
        self.refresh_model_list()
        try:
            model_file = os.path.join(MODELS_DIR_DEFAULT, model + '.bin')
            if os.path.exists(model_file):
                os.remove(model_file)
        except BaseException:
            pass
        try:
            ext_dir = self.settings.get('external_model_dir')
            if ext_dir:
                modellen_ext_dir = os.path.join(ext_dir, 'modellen')
                external_file = os.path.join(modellen_ext_dir, model + '.bin')
                if os.path.exists(external_file):
                    os.remove(external_file)
        except BaseException:
            pass
        messagebox.showinfo('Verwijderen', f"Model '{model}' verwijderd.")
        self.status_var.set(f"Model '{model}' verwijderd.")
        self.model_progress_label.config(text=f"Model '{model}' verwijderd.")

    def create_server_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.Frame(parent, bg=theme['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        tk.Label(frame, text='Serverbeheer', font=self.get_font(), bg=theme
                 ['bg'], fg=theme['fg']).pack(anchor='w', pady=2)
        self.server_vars = {}
        self.timeout_vars = {}
        self.url_vars = {}
        self.port_vars = {}
        self.server_entries = []
        self.ollama_gpu_enabled_vars = {}
        self.ollama_gpu_layers_vars = {}
        self.ollama_gpu_memory_vars = {}
        self.ollama_gpu_batch_vars = {}
        for srv in self.settings['servers']:
            var = tk.BooleanVar(value=self.settings['servers'][srv]['active'])
            self.server_vars[srv] = var
            row = tk.Frame(frame, bg=theme['bg'], highlightbackground=theme
                           ['border'], highlightthickness=1)
            row.pack(fill=tk.X, pady=4, padx=4)
            cb = ttk.Checkbutton(row, text=f'{srv.capitalize()} aan/uit',
                                 variable=var)
            cb.pack(side=tk.LEFT, padx=5)
            tk.Label(row, text='Status:', bg=theme['bg'], fg=theme['fg']).pack(
                side=tk.LEFT)
            lbl = tk.Label(row, textvariable=self.server_status_vars[srv],
                           fg='green' if var.get() else 'red', bg=theme['bg'])
            lbl.pack(side=tk.LEFT, padx=5)
            if srv in ['deepl', 'ollama']:
                tk.Label(row, text='API sleutel:', bg=theme['bg'], fg=theme
                         ['fg']).pack(side=tk.LEFT, padx=2)
                key_var = tk.StringVar(value=self.settings['servers'][srv].
                                       get('key', ''))
                self.url_vars[srv] = key_var
                key_entry = tk.Entry(
                    row,
                    textvariable=key_var,
                    width=24,
                    bg=theme['entry_bg'],
                    fg=theme['entry_fg'],
                    insertbackground=theme['entry_fg'])
                key_entry.pack(side=tk.LEFT)
                self.server_entries.append((srv, 'key', key_var))
            if srv not in ['deepl']:
                tk.Label(row, text='URL:', bg=theme['bg'], fg=theme['fg']
                         ).pack(side=tk.LEFT, padx=2)
                url_var = tk.StringVar(value=self.settings['servers'][srv].
                                       get('url', 'http://127.0.0.1'))
                self.url_vars[srv] = url_var
                url_entry = tk.Entry(
                    row,
                    textvariable=url_var,
                    width=16,
                    bg=theme['entry_bg'],
                    fg=theme['entry_fg'],
                    insertbackground=theme['entry_fg'])
                url_entry.pack(side=tk.LEFT)
                self.server_entries.append((srv, 'url', url_var))
                tk.Label(row, text='Poort:', bg=theme['bg'], fg=theme['fg']
                         ).pack(side=tk.LEFT, padx=2)
                port_var = tk.IntVar(value=self.settings['servers'][srv].
                                     get('port', 0))
                self.port_vars[srv] = port_var
                port_entry = tk.Entry(
                    row,
                    textvariable=port_var,
                    width=6,
                    bg=theme['entry_bg'],
                    fg=theme['entry_fg'],
                    insertbackground=theme['entry_fg'])
                port_entry.pack(side=tk.LEFT)
                self.server_entries.append((srv, 'port', port_var))
            tk.Label(row, text='Timeout:', bg=theme['bg'], fg=theme['fg']
                     ).pack(side=tk.LEFT, padx=2)
            timeout_var = tk.IntVar(value=self.settings['servers'][srv].get
                                    ('timeout', 30))
            self.timeout_vars[srv] = timeout_var
            entry = tk.Entry(
                row,
                textvariable=timeout_var,
                width=5,
                bg=theme['entry_bg'],
                fg=theme['entry_fg'],
                insertbackground=theme['entry_fg'])
            entry.pack(side=tk.LEFT)
            self.server_entries.append((srv, 'timeout', timeout_var))
            if srv == 'ollama':
                gpu_frame = tk.Frame(row, bg=theme['bg'])
                gpu_frame.pack(side=tk.LEFT, padx=4)
                gpu_enabled_var = tk.BooleanVar(value=self.settings[
                    'servers']['ollama']['gpu_support'].get('enabled', False))
                self.ollama_gpu_enabled_vars[srv] = gpu_enabled_var
                gpu_cb = ttk.Checkbutton(
                    gpu_frame, text='GPU?', variable=gpu_enabled_var)
                gpu_cb.pack(side=tk.LEFT, padx=2)
                gpu_layers_var = tk.IntVar(value=self.settings['servers'][
                    'ollama']['gpu_support'].get('num_gpu_layers', 0))
                self.ollama_gpu_layers_vars[srv] = gpu_layers_var
                tk.Label(
                    gpu_frame,
                    text='Layers:',
                    bg=theme['bg'],
                    fg=theme['fg']).pack(
                    side=tk.LEFT,
                    padx=2)
                layers_entry = tk.Entry(
                    gpu_frame,
                    textvariable=gpu_layers_var,
                    width=5,
                    bg=theme['entry_bg'],
                    fg=theme['entry_fg'],
                    insertbackground=theme['entry_fg'])
                layers_entry.pack(side=tk.LEFT)
                gpu_mem_var = tk.StringVar(value=self.settings['servers'][
                    'ollama']['gpu_support'].get('gpu_memory', 'auto'))
                self.ollama_gpu_memory_vars[srv] = gpu_mem_var
                tk.Label(gpu_frame, text='Mem:', bg=theme['bg'], fg=theme['fg']
                         ).pack(side=tk.LEFT, padx=2)
                gpu_mem_combo = ttk.Combobox(
                    gpu_frame,
                    textvariable=gpu_mem_var,
                    values=[
                        'auto',
                        '4GB',
                        '6GB',
                        '8GB',
                        '12GB',
                        '16GB',
                        '24GB',
                        '32GB'],
                    width=6)
                gpu_mem_combo.pack(side=tk.LEFT)
                gpu_batch_var = tk.IntVar(value=self.settings['servers'][
                    'ollama']['gpu_support'].get('gpu_batch_size', 512))
                self.ollama_gpu_batch_vars[srv] = gpu_batch_var
                tk.Label(gpu_frame, text='Batch:', bg=theme['bg'], fg=theme
                         ['fg']).pack(side=tk.LEFT, padx=2)
                batch_entry = tk.Entry(
                    gpu_frame,
                    textvariable=gpu_batch_var,
                    width=5,
                    bg=theme['entry_bg'],
                    fg=theme['entry_fg'],
                    insertbackground=theme['entry_fg'])
                batch_entry.pack(side=tk.LEFT)
        ttk.Button(
            frame,
            text='Status controleren',
            style='Blue.TButton',
            command=self.check_server_status).pack(
            anchor='w',
            padx=5,
            pady=5)
        self.server_status_label = tk.Label(
            frame,
            text='Statuscontrole: niet gestart',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font())
        self.server_status_label.pack(fill=tk.X, padx=8, pady=(2, 0))
        ttk.Button(
            frame,
            text='Opslaan',
            style='Blue.TButton',
            command=self.save_server_settings).pack(
            anchor='w',
            padx=5,
            pady=5)
        ttk.Button(
            frame,
            text='NOODSTOP: Stop ALLES',
            style='Blue.TButton',
            command=lambda: stop_all_model_servers(
                self.settings)).pack(
            anchor='w',
            padx=5,
            pady=10)

    def save_server_settings(self):
        for srv in self.settings['servers']:
            self.settings['servers'][srv]['active'] = self.server_vars[srv
                                                                       ].get()
        for srv, typ, var in self.server_entries:
            if typ == 'url':
                self.settings['servers'][srv]['url'] = var.get()
            elif typ == 'port':
                try:
                    self.settings['servers'][srv]['port'] = int(var.get())
                except BaseException:
                    self.status_var.set('Ongeldige poort waarde.')
            elif typ == 'key':
                self.settings['servers'][srv]['key'] = var.get()
            elif typ == 'timeout':
                try:
                    self.settings['servers'][srv]['timeout'] = int(var.get())
                except BaseException:
                    self.status_var.set('Ongeldige timeout waarde.')
        ollama_cfg = self.settings['servers'].get('ollama', {})
        if 'gpu_support' not in ollama_cfg:
            ollama_cfg['gpu_support'] = {}
        ollama_cfg['gpu_support']['enabled'] = self.ollama_gpu_enabled_vars[
            'ollama'].get()
        ollama_cfg['gpu_support']['num_gpu_layers'
                                  ] = self.ollama_gpu_layers_vars['ollama'].get()
        ollama_cfg['gpu_support']['gpu_memory'] = self.ollama_gpu_memory_vars[
            'ollama'].get()
        ollama_cfg['gpu_support']['gpu_batch_size'
                                  ] = self.ollama_gpu_batch_vars['ollama'].get()
        save_settings(self.settings)
        messagebox.showinfo(
            'Serverbeheer',
            'Serverinstellingen (inclusief GPU-instellingen) opgeslagen.')
        self.status_var.set('Serverinstellingen opgeslagen.')
        self.check_server_status()

    def check_server_status(self):
        self.server_status_label.config(text='Statuscontrole bezig...')

        def do_check():
            for srv in self.settings['servers']:
                status = self.get_server_status(srv)
                self.server_status_vars[srv].set(status)
            self.status_var.set('Serverstatus gecontroleerd.')
            self.server_status_label.config(text='Statuscontrole voltooid!')
        threading.Thread(target=do_check, daemon=True).start()

    def get_server_status(self, srv):
        try:
            if not self.settings['servers'][srv]['active']:
                return 'Uit'
            if srv == 'ollama':
                url = (
                    f"{self.settings['servers'][srv]['url']}:{self.settings['servers'][srv]['port']}/api/tags"
                )
                resp = requests.get(url, timeout=3)
                return 'Online' if resp.status_code == 200 else 'Offline'
            elif srv == 'deepl':
                key = self.settings['servers'][srv]['key']
                if not key:
                    return 'Geen sleutel'
                dd_url = 'https://api-free.deepl.com/v2/usage'
                resp = requests.get(dd_url, params={'auth_key': key}, timeout=3
                                    )
                return 'Online' if resp.status_code == 200 else 'Offline'
            elif srv == 'hugo':
                url = (
                    f"{self.settings['servers'][srv]['url']}:{self.settings['servers'][srv]['port']}/status"
                )
                resp = requests.get(url, timeout=3)
                return 'Online' if resp.status_code == 200 else 'Offline'
            return 'Onbekend'
        except BaseException:
            return 'Offline'

    def create_info_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.Frame(parent, bg=theme['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=16)
        tk.Label(
            frame,
            text='Informatie & Installatie',
            font=self.get_font(),
            bg=theme['bg'],
            fg=theme['accent']).pack(
            anchor='w',
            pady=(
                0,
                8))
        info_texts = [
            ('Ollama (server, modellen):',
             'https://ollama.com/'),
            ('DeepL API (vertaling):',
             'https://www.deepl.com/pro-api'),
            ('HuggingFace (modellen):',
                'https://huggingface.co/models'),
            ('OpenAI GPT (API):',
                'https://platform.openai.com/'),
            ('Llama 2 (Meta, download):',
                'https://ai.meta.com/resources/models-and-libraries/llama-downloads/'),
            ('Mistral AI (modellen):',
             'https://mistral.ai/news/announcing-mistral-7b/'),
            ('Google Translate API:',
                'https://cloud.google.com/translate'),
            ('Meer info over SRT/ASS/VTT:',
             'https://en.wikipedia.org/wiki/SubRip')]
        for label, url in info_texts:
            row = tk.Frame(frame, bg=theme['bg'])
            row.pack(anchor='w', pady=2, fill=tk.X)
            lbl = tk.Label(row, text=label, font=self.get_font(), bg=theme[
                'bg'], fg=theme['fg'], cursor='hand2')
            lbl.pack(side=tk.LEFT)
            link = tk.Label(row, text=url, font=self.get_font(), fg=theme[
                'accent'], bg=theme['bg'], cursor='hand2', underline=True)
            link.pack(side=tk.LEFT, padx=6)

            def open_url(link_url=url):
                webbrowser.open_new(link_url)
            link.bind('<Button-1>', lambda e, link_url=url: open_url(link_url))
        tk.Label(
            frame,
            text='Gebruik steeds de officiële sites voor installatie en modeldownloads.',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font()).pack(
            anchor='w',
            pady=(
                12,
                0))

    def create_filters_and_lists_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        canvas = tk.Canvas(parent, bg=theme['bg'], highlightthickness=0)
        scroll_y = tk.Scrollbar(parent, orient='vertical', command=canvas.yview
                                )
        self.filters_container = tk.Frame(canvas, bg=theme['bg'])
        self.filters_container.bind('<Configure>', lambda e: canvas.
                                    configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=self.filters_container, anchor='nw'
                             )
        canvas.configure(yscrollcommand=scroll_y.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        instruction_label = tk.Label(
            self.filters_container,
            text="""Configureer filter en lijsten:
• Schakel lijsten in/uit voor woordvervanging.
• Voeg evt. eigen termen of zinnen toe.
• Met 'Bewerk' kun je items direct wijzigen.
• Hoofdschakelaar voor filters staat onderaan.""",
            bg=theme['bg'],
            fg=theme['green'],
            justify=tk.LEFT,
            font=self .get_font())
        instruction_label.pack(anchor='w', padx=8, pady=8)
        self.filter_enabled_var = tk.BooleanVar(value=self.filters_config.
                                                get('filters_enabled', True))
        main_chk_frame = tk.Frame(self.filters_container, bg=theme['bg'])
        main_chk_frame.pack(fill=tk.X, padx=8)
        main_filter_chk = ttk.Checkbutton(
            main_chk_frame,
            text='Volledige filter actief (strikte vervangingen)',
            variable=self .filter_enabled_var,
            command=self.toggle_main_filter)
        main_filter_chk.pack(anchor='w', pady=4)
        self.lists_frame = tk.Frame(self.filters_container, bg=theme['bg'])
        self.lists_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=4)
        self.create_paste_and_save_section()
        bottom_bar = tk.Frame(self.filters_container, bg=theme['bg'])
        bottom_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=8, padx=8)
        ttk.Button(
            bottom_bar,
            text='Nieuwe lijst aanmaken',
            style='Blue.TButton',
            command=self.add_new_list).pack(
            side=tk.LEFT,
            padx=4)
        ttk.Button(
            bottom_bar,
            text='Opslaan filterinstellingen',
            style='Blue.TButton',
            command=self.save_filter_settings).pack(
            side=tk .LEFT,
            padx=4)
        self.populate_lists_ui()

    def create_paste_and_save_section(self):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.LabelFrame(
            self.filters_container,
            text='Tekst plakken en opslaan',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font())
        frame.pack(fill=tk.X, padx=8, pady=8)
        label = tk.Label(
            frame,
            text='Plak hieronder vrije tekst en kies een bestandsformaat:',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font())
        label.pack(anchor='w', padx=4, pady=(4, 2))
        scroll_text_frame = tk.Frame(frame, bg=theme['bg'])
        scroll_text_frame.pack(fill=tk.X, padx=4, pady=2)
        self.paste_textbox = tk.Text(
            scroll_text_frame,
            height=8,
            font=self .get_font(),
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['entry_fg'])
        self.paste_textbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        text_scroll = tk.Scrollbar(scroll_text_frame, command=self.
                                   paste_textbox.yview)
        text_scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.paste_textbox.configure(yscrollcommand=text_scroll.set)
        format_label = tk.Label(
            frame,
            text='Formaat:',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font())
        format_label.pack(side=tk.LEFT, padx=(4, 0))
        self.save_format_var = tk.StringVar(value='.srt')
        formats = ['.srt', '.txt', '.json', '.ass', '.vtt']
        format_combo = ttk.Combobox(
            frame,
            values=formats,
            textvariable=self.save_format_var,
            width=6)
        format_combo.pack(side=tk.LEFT, padx=4)
        save_button = ttk.Button(
            frame,
            text='Opslaan',
            style='Blue.TButton',
            command=self.paste_and_save_text)
        save_button.pack(side=tk.LEFT, padx=4, pady=(0, 4))

    def paste_and_save_text(self):
        text_content = self.paste_textbox.get('1.0', tk.END).strip()
        if not text_content:
            messagebox.showwarning('Lege tekst', 'Geen tekst om op te slaan.')
            return
        extension = self.save_format_var.get()
        filename = filedialog.asksaveasfilename(
            title='Tekst opslaan als',
            defaultextension=extension,
            filetypes=[
                ('SRT-bestand',
                 '*.srt'),
                ('Tekstbestand',
                 '*.txt'),
                ('JSON-bestand',
                 '*.json'),
                ('ASS-bestand',
                 '*.ass'),
                ('WebVTT-bestand',
                 '*.vtt'),
                ('Alle bestanden',
                 '*.*')])
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text_content)
                messagebox.showinfo(
                    'Opgeslagen',
                    f'Tekst succesvol opgeslagen als {os.path.basename(filename)}')
                self.status_var.set(
                    f'Tekst succesvol opgeslagen als {os.path.basename(filename)}'
                )
            except Exception as e:
                messagebox.showerror('Fout', f'Fout bij opslaan: {e}')
                self.status_var.set(f'Fout bij opslaan: {e}')

    def populate_lists_ui(self):
        for child in self.lists_frame.winfo_children():
            child.destroy()
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        for idx, list_data in enumerate(self.filters_config.get('lists', [])):
            list_panel = tk.LabelFrame(self.lists_frame, text=list_data[
                'name'], bg=theme['bg'], fg=theme['fg'], font=self.get_font())
            list_panel.pack(fill=tk.X, expand=False, pady=4, padx=4)
            top_list_bar = tk.Frame(list_panel, bg=theme['bg'])
            top_list_bar.pack(fill=tk.X, pady=2)
            enabled_var = tk.BooleanVar(value=list_data.get('enabled', False))
            chk_btn = ttk.Checkbutton(
                top_list_bar,
                text=f"Aan/uit voor '{list_data['name']}'",
                variable=enabled_var,
                command=lambda v=enabled_var,
                i=idx: self. toggle_list_enabled(
                    i,
                    v))
            chk_btn.pack(side=tk.LEFT, padx=4)
            tk.Label(top_list_bar, text='URL:', bg=theme['bg'], fg=theme['fg']
                     ).pack(side=tk.LEFT, padx=4)
            url_var = tk.StringVar(value=list_data.get('source_url', ''))
            url_entry = tk.Entry(
                top_list_bar,
                textvariable=url_var,
                width=50,
                bg=theme['entry_bg'],
                fg=theme['entry_fg'],
                insertbackground=theme['entry_fg'])
            url_entry.pack(side=tk.LEFT, padx=2)

            def save_list_url(list_index=idx, var=url_var):
                self.filters_config['lists'][list_index]['source_url'
                                                         ] = var.get()
                self.status_var.set(
                    f"Bron-URL opgeslagen voor lijst '{self.filters_config['lists'][list_index]['name']}'."
                )
            btn_save_url = ttk.Button(
                top_list_bar,
                text='Opslaan',
                style='Blue.TButton',
                command=save_list_url)
            btn_save_url.pack(side=tk.LEFT, padx=2)

            def open_list_url(uvar=url_var):
                if uvar.get():
                    webbrowser.open_new(uvar.get())
            btn_open_url = ttk.Button(
                top_list_bar,
                text='Openen',
                style='Blue.TButton',
                command=open_list_url)
            btn_open_url.pack(side=tk.LEFT, padx=2)

            def download_list_json(the_index=idx):
                src = self.filters_config['lists'][the_index].get('source_url',
                                                                  '')
                if not src:
                    messagebox.showinfo('Download', 'Geen bron-URL ingevuld.')
                    return
                try:
                    self.status_var.set(f'Downloaden van {src}...')
                    resp = requests.get(src, timeout=15)
                    if resp.status_code == 200:
                        data = resp.json()
                        if isinstance(data, dict):
                            current_dict = self.filters_config['lists'][
                                the_index].get('items', {})
                            merged_count = 0
                            for k, v in data.items():
                                if k not in current_dict:
                                    current_dict[k] = v
                                    merged_count += 1
                            self.filters_config['lists'][the_index]['items'
                                                                    ] = current_dict
                            self.status_var.set(
                                f"{merged_count} nieuwe termen toegevoegd aan lijst '{self.filters_config['lists'][the_index]['name']}'."
                            )
                            messagebox.showinfo(
                                'Download', f'{merged_count} nieuwe termen toegevoegd.')
                            self.populate_lists_ui()
                        else:
                            messagebox.showwarning(
                                'Download', 'JSON was geen dict, kan niet importeren.')
                    else:
                        messagebox.showerror(
                            'Download', f'Foutieve statuscode {resp.status_code} bij ophalen van URL.')
                except Exception as ex:
                    messagebox.showerror('Download',
                                         f'Fout bij downloaden: {ex}')
                    log_error(str(ex), self.settings)
            btn_download = ttk.Button(
                top_list_bar,
                text='Download',
                style='Blue.TButton',
                command=download_list_json)
            btn_download.pack(side=tk.LEFT, padx=2)

            def edit_list_items(the_index=idx):
                edit_win = tk.Toplevel(self)
                edit_win.title(
                    f"Bewerk lijst: {self.filters_config['lists'][the_index]['name']}"
                )
                edit_win.geometry('600x400')
                edit_theme = self.THEMES.get(self.theme_var.get(), self.
                                             THEMES['neo_dark'])
                edit_win.configure(bg=edit_theme['bg'])
                edit_frame = tk.Frame(edit_win, bg=edit_theme['bg'])
                edit_frame.pack(fill=tk.BOTH, expand=True)
                tk.Label(
                    edit_frame,
                    text='Items (key => value):',
                    bg=edit_theme['bg'],
                    fg=edit_theme['fg'],
                    font=self.get_font()).pack(
                    anchor='w')
                lb_frame = tk.Frame(edit_frame, bg=edit_theme['bg'])
                lb_frame.pack(fill=tk.BOTH, expand=True)
                lb = tk.Listbox(
                    lb_frame,
                    height=12,
                    font=self.get_font(),
                    bg=edit_theme['entry_bg'],
                    fg=edit_theme['entry_fg'],
                    selectbackground=edit_theme['accent'])
                lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=4, pady=4
                        )
                scroll_lb = tk.Scrollbar(lb_frame, command=lb.yview)
                scroll_lb.pack(side=tk.LEFT, fill=tk.Y)
                lb.config(yscrollcommand=scroll_lb.set)
                current_items = self.filters_config['lists'][the_index].get(
                    'items', {})
                for k, v in sorted(current_items.items()):
                    lb.insert(tk.END, f'{k} => {v}')
                btn_side = tk.Frame(lb_frame, bg=edit_theme['bg'])
                btn_side.pack(side=tk.LEFT, fill=tk.Y)

                def add_item():
                    old_word = simpledialog.askstring(
                        'Oude term', 'Voer de bron-term in:', parent=edit_win)
                    if old_word is None:
                        return
                    new_word = simpledialog.askstring(
                        'Nieuwe term', f"Waarmee '{old_word}' vervangen?:", parent=edit_win)
                    if new_word is None:
                        return
                    if old_word.strip():
                        current_items[old_word] = new_word
                        lb.insert(tk.END, f'{old_word} => {new_word}')
                        self.status_var.set(f"Term '{old_word}' toegevoegd.")
                    else:
                        messagebox.showwarning(
                            'Lege key', 'Key/term mag niet leeg zijn.', parent=edit_win)

                def remove_item():
                    sel = lb.curselection()
                    if not sel:
                        return
                    line = lb.get(sel[0])
                    if '=>' in line:
                        oldw, neww = line.split('=>', 1)
                        oldw, neww = oldw.strip(), neww.strip()
                        if oldw in current_items:
                            del current_items[oldw]
                        lb.delete(sel[0])
                        self.status_var.set(f"Term '{oldw}' verwijderd.")
                ttk.Button(btn_side, text='Toevoegen', style='Blue.TButton',
                           command=add_item).pack(fill=tk.X, pady=2)
                ttk.Button(
                    btn_side,
                    text='Verwijderen',
                    style='Blue.TButton',
                    command=remove_item).pack(
                    fill=tk.X,
                    pady=2)

                def save_edit():
                    self.filters_config['lists'][the_index]['items'
                                                            ] = current_items
                    self.populate_lists_ui()
                    save_filters_config(self.filters_config)
                    messagebox.showinfo(
                        'Bewerken', 'Wijzigingen opgeslagen.', parent=edit_win)
                    edit_win.destroy()
                ttk.Button(
                    edit_frame,
                    text='Sluiten [Opslaan]',
                    style='Blue.TButton',
                    command=save_edit).pack(
                    pady=4)
            btn_edit = ttk.Button(
                top_list_bar,
                text='Bewerk',
                style='Blue.TButton',
                command=edit_list_items)
            btn_edit.pack(side=tk.LEFT, padx=2)

    def toggle_list_enabled(self, list_index, boolvar):
        self.filters_config['lists'][list_index]['enabled'] = boolvar.get()
        self.status_var.set(
            f"Lijst '{self.filters_config['lists'][list_index]['name']}' staat nu op {'aan' if boolvar.get() else 'uit'}."
        )

    def toggle_main_filter(self):
        self.filters_config['filters_enabled'] = self.filter_enabled_var.get()
        self.status_var.set(
            f"Hoofd filter staat nu op {'ingeschakeld' if self.filter_enabled_var.get() else 'uitgeschakeld'}."
        )

    def add_new_list(self):
        name = simpledialog.askstring(
            'Nieuwe lijst',
            'Voer de naam in voor de nieuwe filterlijst:')
        if not name:
            return
        new_entry = {'name': name, 'enabled': True, 'file_format': 'json',
                     'source_url': '', 'items': {}}
        self.filters_config['lists'].append(new_entry)
        self.populate_lists_ui()
        self.status_var.set(f"Nieuwe lijst '{name}' is aangemaakt.")

    def save_filter_settings(self):
        save_filters_config(self.filters_config)
        messagebox.showinfo('Filters en lijsten',
                            'Filterinstellingen opgeslagen.')
        self.status_var.set('Filterinstellingen opgeslagen.')

    def create_list_converter_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        canvas = tk.Canvas(parent, bg=theme['bg'], highlightthickness=0)
        scroll_y = tk.Scrollbar(parent, orient='vertical', command=canvas.yview
                                )
        self.lijst_convertor_container = tk.Frame(canvas, bg=theme['bg'])
        self.lijst_convertor_container.bind(
            '<Configure>', lambda e: canvas .configure(
                scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=self.lijst_convertor_container,
                             anchor='nw')
        canvas.configure(yscrollcommand=scroll_y.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        tk.Label(self.lijst_convertor_container, text=f"""Lijst Convertor:
Voer hieronder regels in het formaat:
  Term => Beschrijving

Voorbeeld:
  AAW => Anti-Air Warfare
  Beta => Bèta
  Python => Een programmeertaal

Klik op 'Genereer JSON Structuur' voor een dictionary.
Gebruik 'Opslaan in map' om als .json op te slaan in:
  {LIST_CONVERTER_EXPORT_DIR}

Bij ontbrekende '=>' kun je 'Auto-format' aanvinken: splitst op de eerste spatie.""", bg=theme['bg'], fg=theme['fg'], font=self.get_font(), justify=tk.LEFT).pack(anchor='w', padx=16, pady=(8, 12))
        tk.Label(
            self.lijst_convertor_container,
            text='Kies een voorbeeldformaat:',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font()).pack(
            anchor='w',
            padx=16)
        self.example_choice_var = tk.StringVar(value='AAW => Anti-Air Warfare')
        combo_values = [
            'AAW => Anti-Air Warfare',
            'Beta => Bèta',
            'Python => Een programmeertaal',
            'Custom: leeg invoerveld']
        self.example_choice_combo = ttk.Combobox(
            self. lijst_convertor_container,
            values=combo_values,
            textvariable=self.example_choice_var,
            width=40)
        self.example_choice_combo.pack(anchor='w', padx=16, pady=(2, 8))

        def insert_example():
            choice = self.example_choice_var.get()
            if choice.startswith('Custom'):
                self.lijst_convertor_text.delete('1.0', tk.END)
            else:
                self.lijst_convertor_text.delete('1.0', tk.END)
                self.lijst_convertor_text.insert('1.0', choice)
        insert_btn_frame = tk.Frame(
            self.lijst_convertor_container, bg=theme['bg'])
        insert_btn_frame.pack(fill=tk.X, padx=16, pady=(0, 8))
        ttk.Button(
            insert_btn_frame,
            text='Voorbeeld invoegen',
            style='Blue.TButton',
            command=insert_example).pack(
            side=tk.LEFT,
            ipadx=8)
        text_frame = tk.Frame(self.lijst_convertor_container, bg=theme['bg'])
        text_frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=4)
        scroll = tk.Scrollbar(text_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lijst_convertor_text = tk.Text(
            text_frame,
            height=12,
            font=self.get_font(),
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['entry_fg'],
            yscrollcommand=scroll.set)
        self.lijst_convertor_text.pack(fill=tk.BOTH, expand=True)
        scroll.config(command=self.lijst_convertor_text.yview)
        self.auto_format_var = tk.BooleanVar(value=False)
        auto_format_frame = tk.Frame(
            self.lijst_convertor_container, bg=theme['bg'])
        auto_format_frame.pack(fill=tk.X, padx=16, pady=(4, 8))
        auto_format_chk = ttk.Checkbutton(
            auto_format_frame,
            text='Auto-format (als => ontbreekt, splits op eerste spatie)',
            variable=self.auto_format_var)
        auto_format_chk.pack(side=tk.LEFT, padx=6)
        button_frame = tk.Frame(self.lijst_convertor_container, bg=theme['bg'])
        button_frame.pack(fill=tk.X, padx=16, pady=8)
        self.generate_button = ttk.Button(
            button_frame,
            text='Genereer JSON Structuur',
            style='Blue.TButton',
            command=self. generate_json_from_input)
        self.generate_button.pack(side=tk.LEFT, padx=4, ipady=5)
        self.save_button = ttk.Button(
            button_frame,
            text='Opslaan in map',
            style='Blue.TButton',
            command=self.save_generated_json)
        self.save_button.pack(side=tk.LEFT, padx=4, ipady=5)
        self.generated_json = {}
        self.convertor_status = tk.Label(
            self.lijst_convertor_container,
            text='',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font())
        self.convertor_status.pack(anchor='w', padx=16, pady=4)

    def generate_json_from_input(self):
        import re
        raw_text = self.lijst_convertor_text.get('1.0', tk.END).strip()
        lines = raw_text.splitlines()
        result_dict = {}
        for line in lines:
            line = re.sub('[.-]+', '', line)
            line = line.strip()
            if '=>' in line:
                parts = line.split('=>', 1)
                key = parts[0].strip()
                val = parts[1].strip()
                if key:
                    result_dict[key] = val
            elif self.auto_format_var.get():
                splitted = line.split(None, 1)
                if len(splitted) == 2:
                    k, v = splitted
                    k, v = k.strip(), v.strip()
                    if k:
                        result_dict[k] = v
        self.generated_json = result_dict
        count_keys = len(result_dict.keys())
        if count_keys > 0:
            messagebox.showinfo(
                'JSON Klaar',
                f'JSON structuur gegenereerd met {count_keys} items.')
        else:
            messagebox.showwarning(
                'Geen items',
                'Er zijn 0 geldige items aangetroffen. Controleer je input of schakel auto-format in.')
        self.convertor_status.config(
            text=f'JSON structuur gegenereerd met {count_keys} items.')
        self.status_var.set(
            f'Lijst Convertor: JSON structuur gegenereerd met {count_keys} items.'
        )

    def save_generated_json(self):
        if not self.generated_json:
            messagebox.showwarning(
                'Geen JSON',
                "Er is geen JSON structuur. Klik eerst op 'Genereer JSON Structuur'.")
            return
        filename = simpledialog.askstring(
            'Bestandsnaam',
            'Voer een bestandsnaam in (zonder extensie, bijv. MyList):')
        if not filename:
            return
        json_path = os.path.join(LIST_CONVERTER_EXPORT_DIR, filename + '.json')
        try:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(self.generated_json, f, indent=2, ensure_ascii=False)
            messagebox.showinfo('Opgeslagen',
                                f'JSON lijst opgeslagen als:\n{json_path}')
            self.status_var.set(
                f'JSON lijst opgeslagen in list_converter_export: {os.path.basename(json_path)}'
            )
        except Exception as e:
            messagebox.showerror('Fout', f'Fout bij opslaan: {e}')
            log_error(str(e), self.settings)

    def create_spellcheck_tab(self, parent):
        theme = self.THEMES.get(self.theme_var.get(), self.THEMES['neo_dark'])
        frame = tk.Frame(parent, bg=theme['bg'])
        frame.pack(fill=tk.BOTH, expand=True)
        lbl_info = tk.Label(
            frame,
            text="""Spellingcontrole over de volledige ondertitel:
• Kies een spellingcontrole-taal (handmatig of Automatisch).
• Corrigeer spelling m.b.v. LanguageTool (andere talen) of pyspellchecker (Engels).
• Filters worden ook toegepast.

Laad eerst een ondertitelbestand (Bestand > Open ondertitel...)""",
            fg=theme['fg'],
            bg=theme['bg'],
            font=self.get_font())
        lbl_info.pack(anchor='w', padx=8, pady=8)
        topbar = tk.Frame(frame, bg=theme['bg'])
        topbar.pack(fill=tk.X, pady=(8, 8))
        tk.Label(topbar, text='Spelling-taal:', bg=theme['bg'], fg=theme[
            'fg'], font=self.get_font()).pack(side=tk.LEFT, padx=(2, 4))
        self.spellcheck_language_var = tk.StringVar(value='Automatisch')
        available_spelling_langs = [
            'Automatisch',
            'Nederlands',
            'Engels',
            'Duits',
            'Frans',
            'Spaans',
            'Italiaans',
            'Portugees',
            'Pools',
            'Russisch',
            'Japans',
            'Chinees']
        self.spellcheck_lang_combo = ttk.Combobox(
            topbar,
            values=available_spelling_langs,
            textvariable=self. spellcheck_language_var,
            width=16)
        self.spellcheck_lang_combo.pack(side=tk.LEFT, padx=4)
        btn_spellcheck = ttk.Button(
            topbar,
            text='Spellingcontrole starten',
            style='Blue.TButton',
            command=self.live_spellcheck_subtitle)
        btn_spellcheck.pack(side=tk.LEFT, padx=6, ipadx=8, ipady=4)
        btn_stop_spellcheck = ttk.Button(
            topbar,
            text='Stop',
            style='Blue.TButton',
            command=self.stop_spellcheck)
        btn_stop_spellcheck.pack(side=tk.LEFT, padx=6, ipadx=8, ipady=4)
        btn_clear_spellcheck = ttk.Button(
            topbar,
            text='Wis',
            style='Blue.TButton',
            command=self.clear_spellcheck_text)
        btn_clear_spellcheck.pack(side=tk.LEFT, padx=6, ipadx=8, ipady=4)
        btn_save_spellcheck = ttk.Button(
            topbar,
            text='Opslaan als SRT',
            style='Blue.TButton',
            command=self.save_spellcheck_text_as_srt)
        btn_save_spellcheck.pack(side=tk.LEFT, padx=6, ipadx=8, ipady=4)
        self.spellcheck_text = tk.Text(
            frame,
            height=30,
            font=self.get_font(),
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['entry_fg'])
        self.spellcheck_text.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        spellcheck_scroll = tk.Scrollbar(self.spellcheck_text, command=self
                                         .spellcheck_text.yview)
        self.spellcheck_text.configure(yscrollcommand=spellcheck_scroll.set)
        spellcheck_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        bottom = tk.Frame(frame, bg=theme['bg'])
        bottom.pack(fill=tk.X, pady=4)
        self.progress_spellcheck_var = tk.DoubleVar(value=0)
        self.progress_spellcheck_label = tk.Label(
            bottom,
            text='0/0 regels gecontroleerd',
            bg=theme['bg'],
            fg=theme['fg'],
            font=self.get_font())
        self.progress_spellcheck_label.pack(side=tk.LEFT, padx=8)
        self.progress_spellcheck_bar = ttk.Progressbar(
            bottom,
            variable=self.progress_spellcheck_var,
            maximum=100,
            style='blue.Horizontal.TProgressbar')
        self.progress_spellcheck_bar.pack(fill=tk.X, expand=True, padx=8,
                                          side=tk.LEFT)

    def stop_spellcheck(self):
        self.spellcheck_stop_event.set()
        self.status_var.set('Spellingcontrole stoppen aangevraagd.')

    def clear_spellcheck_text(self):
        self.spellcheck_text.delete('1.0', tk.END)
        self.status_var.set('Spellingcontrole-tekst gewist.')

    def live_spellcheck_subtitle(self):
        if not self.current_subs:
            messagebox.showwarning('Geen ondertitels',
                                   'Laad eerst een ondertitelbestand.')
            self.status_var.set('Geen ondertitel geladen.')
            return
        if self.spellcheck_in_progress.is_set():
            messagebox.showwarning('Spellingcontrole bezig',
                                   'Er is al een spellingcontrole bezig.')
            return
        self.spellcheck_stop_event.clear()
        self.spellcheck_in_progress.set()
        self.spellcheck_text.delete('1.0', tk.END)
        lines = list(self.current_subs)
        total = len(lines)
        self.progress_spellcheck_var.set(0)
        self.progress_spellcheck_label.config(
            text=f'0/{total} regels gecontroleerd.')
        self.status_var.set(f'Spellingcontrole gestart: 0/{total} regels.')
        chosen_lang = self.spellcheck_language_var.get()
        self.spellchecked_subs = pysubs2.SSAFile()

        def do_spellcheck():
            for idx, line in enumerate(lines):
                if self.spellcheck_stop_event.is_set():
                    self.status_var.set('Spellingcontrole gestopt.')
                    self.spellcheck_in_progress.clear()
                    return
                raw_line = line.text
                filtered_line = apply_filter_lists(raw_line, self.
                                                   filters_config)
                if not filtered_line.strip():
                    filtered_line = raw_line
                if chosen_lang == 'Automatisch':
                    try:
                        if filtered_line.strip():
                            possible_langs_line = detect_langs(filtered_line)
                            if possible_langs_line:
                                best_line_match = max(possible_langs_line,
                                                      key=lambda l: l.prob)
                                line_lang_name = map_detected_language_code(
                                    best_line_match.lang)
                            else:
                                line_lang_name = 'Engels'
                        else:
                            line_lang_name = 'Engels'
                    except BaseException:
                        line_lang_name = 'Engels'
                else:
                    line_lang_name = chosen_lang
                spelled_line = correct_spelling(
                    filtered_line, line_lang_name, self.settings, self)
                spelled_line = re.sub(r'\\s+', ' ', spelled_line).strip()
                srt_line = f"""{idx + 1}
{srt_time(line.start)} --> {srt_time(line.end)}
{spelled_line}

"""
                self.spellcheck_text.insert(tk.END, srt_line)
                new_line = line.copy()
                new_line.text = spelled_line
                self.spellchecked_subs.append(new_line)
                self.progress_spellcheck_var.set((idx + 1) / total * 100)
                self.progress_spellcheck_label.config(
                    text=f'{idx + 1}/{total} regels gecontroleerd.')
                self.status_var.set(
                    f'Spellingcontrole: regel {idx + 1}/{total}.')
                self.update_idletasks()
            self.status_var.set('Spellingcontrole voltooid.')
            messagebox.showinfo('Spellingcontrole',
                                'De spellingcontrole is klaar!')
            self.spellcheck_in_progress.clear()
        threading.Thread(target=do_spellcheck, daemon=True).start()

    def save_spellcheck_text_as_srt(self):
        if not self.spellchecked_subs or len(self.spellchecked_subs) == 0:
            messagebox.showwarning(
                'Leeg', 'Geen spelling-gecorrigeerde ondertitels om op te slaan.')
            return
        filename = filedialog.asksaveasfilename(
            title='Spellingcontrole-resultaat opslaan als SRT',
            defaultextension='.srt',
            filetypes=[
                ('SubRip (.srt)',
                 '*.srt'),
                ('Alle bestanden',
                 '*.*')])
        if not filename:
            return
        success, err = export_subs(self.spellchecked_subs, filename)
        if success:
            messagebox.showinfo(
                'Opgeslagen',
                f'Bestand is opgeslagen als: {os.path.basename(filename)}')
            self.status_var.set(
                f'Spellingcontrole-bestand opgeslagen als: {os.path.basename(filename)}'
            )
        else:
            messagebox.showerror('Fout', f'Fout bij opslaan: {err}')
            self.status_var.set(f'Fout bij opslaan: {err}')

    def download_script(self):
        pw = simpledialog.askstring(
            'Admin Password',
            'Geef het Admin-wachtwoord om het script te downloaden:',
            show='*')
        if not pw:
            messagebox.showwarning('Afgebroken',
                                   'Download geannuleerd door gebruiker.')
            return
        if not check_admin_password(pw):
            messagebox.showerror(
                'Ongeldig wachtwoord',
                'Admin-wachtwoord is onjuist. Toegang geweigerd.')
            return
        filename = filedialog.asksaveasfilename(title='Script opslaan als',
                                                defaultextension='.py')
        if not filename:
            return
        if getattr(sys, 'frozen', False) and self.settings.get(
                'script_download_if_exe', True):
            try:
                script_content = ALL_SCRIPT_SOURCE.encode(
                    'utf-8', errors='replace')
                with open(filename, 'wb') as dst:
                    dst.write(script_content)
                messagebox.showinfo(
                    'Script',
                    f'Originele .py script is opgeslagen als {os.path.basename(filename)} (EXE-modus).')
                self.status_var.set(
                    f'Originele .py script opgeslagen als {os.path.basename(filename)}.'
                )
            except Exception as e:
                messagebox.showerror('Fout', f'Fout bij opslaan: {e}')
                self.status_var.set(f'Fout bij opslaan: {e}')
            return
        try:
            script_path = getattr(sys, 'frozen', False
                                  ) and sys.executable or __file__
            with open(script_path, 'rb') as src, open(filename, 'wb') as dst:
                dst.write(src.read())
            messagebox.showinfo(
                'Script', f'Script opgeslagen als {os.path.basename(filename)}')
        except Exception as e:
            messagebox.showerror('Fout', f'Fout bij opslaan: {e}')

    def save_error_log(self):
        filename = filedialog.asksaveasfilename(
            title='Foutlog opslaan als', defaultextension='.log', filetypes=[
                ('Log bestanden', '*.log'), ('Tekst bestanden', '*.txt'), ('Alle bestanden', '*.*')])
        if filename:
            try:
                if not os.path.exists(self.settings['error_log']):
                    with open(self.settings['error_log'], 'w', encoding='utf-8'
                              ):
                        pass
                with open(self.settings['error_log'], 'r', encoding='utf-8'
                          ) as src:
                    content = src.read()
                with open(filename, 'w', encoding='utf-8') as dst:
                    dst.write(content)
                messagebox.showinfo(
                    'Foutlog', f'Foutlog opgeslagen als {os.path.basename(filename)}')
            except Exception as e:
                messagebox.showerror('Fout', f'Fout bij opslaan: {e}')
                self.status_var.set(f'Fout bij opslaan: {e}')

    def open_settings(self):
        win = tk.Toplevel(self)
        win.title('Instellingen')
        win.geometry('420x500')
        tk.Label(win, text='Thema:').pack(anchor='w', padx=10, pady=(10, 0))
        theme_combo = ttk.Combobox(win, values=list(self.THEMES.keys()),
                                   textvariable=self.theme_var)
        theme_combo.pack(fill=tk.X, padx=10)
        tk.Label(win, text='Lettertype:').pack(anchor='w', padx=10, pady=(
            10, 0))
        import tkinter.font as tkfont
        font_choices = sorted(set(['Segoe UI',
                                   'Arial',
                                   'Calibri',
                                   'Consolas',
                                   'Courier New',
                                   'Comic Sans MS',
                                   'Verdana',
                                   'Tahoma',
                                   'Times New Roman',
                                   'Lucida Console',
                                   'Helvetica',
                                   'Georgia',
                                   'Impact',
                                   'Trebuchet MS',
                                   'Palatino Linotype',
                                   'Book Antiqua'] + list(tkfont.families())))
        font_entry = ttk.Combobox(
            win,
            values=font_choices,
            textvariable=self.font_family)
        font_entry.pack(fill=tk.X, padx=10)
        tk.Label(
            win,
            text='Lettergrootte:').pack(
            anchor='w',
            padx=10,
            pady=(
                10,
                0))
        font_size_entry = tk.Entry(win, textvariable=self.font_size)
        font_size_entry.pack(fill=tk.X, padx=10)
        tk.Label(win, text='Tekststijl:').pack(anchor='w', padx=10, pady=(
            10, 0))
        style_combo = ttk.Combobox(
            win,
            values=[
                'normaal',
                'vet',
                'cursief',
                'vet cursief',
                'onderstreept',
                'vet onderstreept',
                'cursief onderstreept',
                'vet cursief onderstreept'],
            textvariable=self.text_style)
        style_combo.pack(fill=tk.X, padx=10)
        tk.Label(
            win,
            text='Doeltaal (standaard):').pack(
            anchor='w',
            padx=10,
            pady=(
                10,
                0))
        target_combo = ttk.Combobox(
            win,
            values=[
                'Nederlands',
                'Engels',
                'Duits',
                'Frans',
                'Spaans',
                'Italiaans',
                'Portugees',
                'Pools',
                'Russisch',
                'Japans',
                'Chinees'],
            textvariable=self.target_lang_var)
        target_combo.pack(fill=tk.X, padx=10)

        def save_and_close():
            self.settings['theme'] = self.theme_var.get()
            self.settings['font_family'] = self.font_family.get()
            self.settings['font_size'] = self.font_size.get()
            self.settings['text_style'] = self.text_style.get()
            self.settings['target_language'] = self.target_lang_var.get()
            save_settings(self.settings)
            self.apply_theme()
            self.update_fonts()
            self.status_var.set('Instellingen opgeslagen.')
            win.destroy()
        ttk.Button(
            win,
            text='Opslaan',
            style='Blue.TButton',
            command=save_and_close).pack(
            pady=16)
        ttk.Button(win, text='Annuleren', command=win.destroy).pack()

    def reset_settings(self):
        save_settings(DEFAULT_SETTINGS)
        self.settings = load_settings()
        save_filters_config(DEFAULT_FILTER_CONFIG)
        self.filters_config = load_filters_config()
        self.font_family.set(self.settings['font_family'])
        self.font_size.set(self.settings['font_size'])
        self.text_style.set(self.settings['text_style'])
        self.theme_var.set(self.settings['theme'])
        self.target_lang_var.set(self.settings['target_language'])
        self.apply_theme()
        self.refresh_model_list()
        self.populate_lists_ui()
        self.status_var.set(
            'Instellingen zijn teruggezet naar standaardwaarden.')


def update_script_string():
    """
    Replaces the content of ALL SCRIPT SOURCE in this file
    with the full contents of this script itself.
    """
    script_path = os.path.abspath(__file__)
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
    except Exception as e:
        print(f"Fout bij het lezen van het script: {e}")
        return

    # Regex: werkt met zowel ''' als """
    pattern = r"ALL SCRIPT SOURCE\s*=\s*(?P<quote>'''|\"\"\")(?P<body>.*?)(?P=quote)"

    def replacement_func(match):
        # Gebruik altijd drie enkele quotes voor de nieuwe string
        return f"ALL SCRIPT SOURCE = '''{script_content}'''"

    if re.search(pattern, script_content, flags=re.DOTALL):
        new_content = re.sub(
            pattern,
            replacement_func,
            script_content,
            flags=re.DOTALL)
        actie = "geüpdatet"
    else:
        new_content = script_content.rstrip() + "\n\n" + \
            f"ALL SCRIPT SOURCE = '''{script_content}'''"
        actie = "toegevoegd"

    try:
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(
            f"ALL SCRIPT SOURCE is nu {actie} met de volledige script-inhoud.")
    except Exception as e:
        print(f"Fout bij het schrijven van het script: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "update":
        update_script_string()
    else:
        try:
            app = SubtitleTranslatorPro()
            app.mainloop()
        except Exception as e:
            print(f"Fout bij het starten van de applicatie: {e}")
