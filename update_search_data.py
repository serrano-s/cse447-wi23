"""
There's a very high chance this script is reinventing the wheel, but it does what it's supposed to
and saved me the trouble of figuring out whether/how jekyll automatically supports this kind of update.
Use at your own risk.
Note that, among other things, this script assumes we don't have any inline comments in calendar.yml.
"""
from string import punctuation
import json


staffer_order = [('sofia', 'Instructor'), ('daksh', 'Teaching Assistant'), ('khirod', 'Teaching Assistant'),
                 ('leo', 'Teaching Assistant'), ('leroy', 'Teaching Assistant'), ('urmika', 'Teaching Assistant'),
                 ('velocity', 'Teaching Assistant')]
fname_to_write_to = 'assets/js/search-data.json'
list_of_json_dicts = []


def clean_comments_off_end_of_line(l):
    l = l.strip()
    in_string = False
    part_of_line_to_save = ''
    if l.startswith("'"):
        # assume this is a string marker
        in_string = True
        string_marker = "'"
    elif l.startswith('"'):
        in_string = True
        string_marker = '"'
    if in_string:
        # look for which parts of this line are likely a string and set those aside
        prev_char = string_marker
        second_unescaped_str_marker_ind = None
        for ind_minus_1, char in enumerate(l[1:]):
            char_ind = ind_minus_1 + 1
            if char == string_marker and prev_char != '\\':
                second_unescaped_str_marker_ind = char_ind
            prev_char = char
        if second_unescaped_str_marker_ind is not None:
            # then we have a string to set aside
            part_of_line_to_save = l[:second_unescaped_str_marker_ind + 1]
            l = l[second_unescaped_str_marker_ind + 1:]
    if '#' in l and l.count('&#') < l.count('#'):
        # find the first index that's a # without a & before it
        prev_char = ''
        ind_we_want = None
        for i in range(len(l)):
            if l[i] == '#' and prev_char != '&':
                ind_we_want = i
                break
            prev_char = l[i]
        assert ind_we_want is not None
        l = part_of_line_to_save + l[:ind_we_want]
    l = l.strip()
    return l


def clean_line(l):
    if l.startswith('"') and l.endswith('"'):
        l = l[1: -1]
        l = l.replace('\\"', '"')
    elif l.startswith("'") and l.endswith("'"):
        l = l[1: -1]
        l = l.replace("\\'", "'")
    else:
        l = l.replace('&#58;', ':')
    return l


# First read through config and staffer files for top-level details
doc = None
cur_section_name = None
first_part_of_url = None
second_part_of_url = None
with open('_config.yml', 'r') as f:
    for line in f:
        if line.startswith('title :') or line.startswith('title:'):
            doc = clean_comments_off_end_of_line(line[line.index(':') + 1:].strip())
        elif line.startswith('tagline :') or line.startswith('tagline:'):
            cur_section_name = clean_comments_off_end_of_line(line[line.index(':') + 1:].strip())
        elif line.startswith('url :') or line.startswith('url:'):
            first_part_of_url = clean_comments_off_end_of_line(line[line.index(':') + 1:].strip())
        elif line.startswith('baseurl :') or line.startswith('baseurl:'):
            second_part_of_url = clean_comments_off_end_of_line(line[line.index(':') + 1:].strip())
        if doc is not None and cur_section_name is not None and \
                first_part_of_url is not None and second_part_of_url is not None:
            break
assert doc is not None and cur_section_name is not None and first_part_of_url is not None and \
       second_part_of_url is not None
doc, cur_section_name, first_part_of_url, second_part_of_url = \
    clean_line(doc), clean_line(cur_section_name), clean_line(first_part_of_url), clean_line(second_part_of_url)
base_url_of_course = first_part_of_url
if base_url_of_course.endswith('/'):
    if second_part_of_url.startswith('/'):
        second_part_of_url = second_part_of_url[1:]
elif not base_url_of_course.endswith('/'):
    if not second_part_of_url.startswith('/'):
        second_part_of_url = '/' + second_part_of_url
base_url_of_course += second_part_of_url
if base_url_of_course.endswith('/'):
    base_url_of_course = base_url_of_course[:-1]
rel_url = cur_section_name.lower()
for char in punctuation:
    if char == '-':
        continue
    rel_url = rel_url.replace(char, '')
rel_url = '/#' + rel_url.replace(' ', '-')


# note that this method assumes we don't have any inline comments in calendar.yml.
def add_calendar_content(cur_content):
    # add to cur_content
    to_add = ' | Week | Date | Topics | Readings | Homeworks | '
    in_topics_section = False
    with open('_data/calendar.yml', 'r') as cal_f:
        cur_week = None
        row_week = None
        row_date = None
        row_topic = None
        row_slides = None
        row_recording = None
        row_supplement = None
        row_readings = None
        row_hw = None
        for line in cal_f:
            line = line.strip()

            line_header = line[1:].strip() if line.startswith('-') else line
            if in_topics_section and not (line_header.startswith('title') or line_header.startswith('link')):
                in_topics_section = False

            if line.startswith('- week:'):
                week_num = line[line.index(':') + 1:].strip()
                cur_week = week_num
            elif line.startswith('- date:'):
                # then time to compile
                if row_date is None:
                    # then this is our first time around.
                    row_date = line[line.index(':') + 1:].strip()
                    if cur_week is not None:
                        row_week = cur_week
                        cur_week = None
                    else:
                        row_week = None
                        cur_week = None
                    continue
                row_str = '. | '
                if row_week is not None:
                    row_str += row_week + ' | '
                row_str += row_date + ' | ' + row_topic + ' '
                if row_slides is not None:
                    row_str += '[slides] '
                if row_recording is not None:
                    row_str += '[recording] '
                if row_supplement is not None:
                    row_str += '[supplementary recording] '
                row_str += '| '
                if row_readings is not None:
                    row_str += row_readings.replace('&', '&amp;') + ' | '
                else:
                    row_str += '| '
                if row_hw is not None:
                    row_str += row_hw + ' | '
                else:
                    row_str += '| '
                to_add += row_str
                if cur_week is not None:
                    row_week = cur_week
                    cur_week = None
                else:
                    row_week = None
                    cur_week = None
                row_date = line[line.index(':') + 1:].strip()
                row_topic = None
                row_slides = None
                row_recording = None
                row_supplement = None
                row_readings = None
                row_hw = None
            elif line.startswith('topics:'):
                row_topic = line[line.index(':') + 1:].strip()
                in_topics_section = True
            elif line.startswith('slides:') and line[line.index(':') + 1:].strip() != '':
                row_slides = True
            elif line.startswith('recording:') and line[line.index(':') + 1:].strip() != '':
                row_recording = True
            elif line.startswith('supplement:') and line[line.index(':') + 1:].strip() != '':
                row_supplement = True
            elif line.startswith('due:') and line[line.index(':') + 1:].strip() != '':
                row_hw = line[line.index(':') + 1:].strip()
            elif line.startswith('- title:') and line[line.index(':') + 1:].strip() != '':
                if in_topics_section:
                    bit_to_add = line[line.index(':') + 1:].strip()[1:-1].replace('\\"', '"')
                    row_topic += bit_to_add
                else:
                    if row_readings is None:
                        row_readings = line[line.index(':') + 1:].strip()
                    else:
                        row_readings += '; ' + line[line.index(':') + 1:].strip()
    assert row_date is not None and row_topic is not None
    row_str = '. | '
    if row_week is not None:
        row_str += row_week + ' | '
    row_str += row_date + ' | ' + row_topic + ' '
    if row_slides is not None:
        row_str += '[slides] '
    if row_recording is not None:
        row_str += '[recording] '
    if row_supplement is not None:
        row_str += '[supplementary recording] '
    row_str += '| '
    if row_readings is not None:
        row_str += row_readings.replace('&', '&amp;') + ' | '
    else:
        row_str += '| '
    if row_hw is not None:
        row_str += row_hw + ' | '
    else:
        row_str += '| '
    to_add += row_str
    return cur_content + to_add + '. '


def get_staff_member_info(staff_mem):
    staff_mem_file = '_staffers/' + staff_mem + '.md'
    str_representing_staff_mem_info = ''
    staffer_name = None
    email = None
    staffer_role = None
    office_hours = None
    with open(staff_mem_file, 'r') as staff_f:
        # pull role, email, name, office hours
        for line in staff_f:
            if line.startswith('name:'):
                staffer_name = line[line.index(':') + 1:].strip()
            elif line.startswith('role:'):
                staffer_role = line[line.index(':') + 1:].strip()
            elif line.startswith('email'):
                email = line[line.index(':') + 1:].strip()
            elif line.startswith('Office hours:') or line.startswith('OH:'):
                office_hours = line.strip()
    assert staffer_name is not None and email is not None and staffer_role is not None and office_hours is not None
    return staffer_role + ':&nbsp; ' + staffer_name + ' . ' + email + ' . ' + office_hours + ' . '


def clean_out_formatting(l):
    # first get rid of any hyperlinks
    if '](' in l:
        # we assume any ] in the line represents the end of hyperlinked text.
        while '](' in l:
            start_looking = l.index('](')
            beginning_bracket_ind = None
            for i in range(start_looking, -1, -1):
                if l[i] == '[':
                    beginning_bracket_ind = i
                    break
            assert beginning_bracket_ind is not None
            end_paren_ind = None
            for i in range(start_looking + 2, len(l)):
                if l[i] == ')':
                    end_paren_ind = i
                    break
            assert end_paren_ind is not None
            l = l[:beginning_bracket_ind] + l[beginning_bracket_ind + 1: start_looking] + l[end_paren_ind + 1:]
    return l.replace('**', '').replace('_', '')


cur_content = ""
in_comment_block = False
number_of_hyphen_lines_passed = 0
with open('index.md', 'r') as f:
    for line in f:
        if number_of_hyphen_lines_passed < 2:
            if line.startswith('---'):
                number_of_hyphen_lines_passed += 1
            continue

        if not in_comment_block:
            # look for the start of a comment block
            if '<!--' in line:
                in_comment_block = True
                templine = line[line.index('<!--') + 4:]
                if '-->' in templine:
                    in_comment_block = False
                line = line[:line.index('<!--')]
                if '-->' in templine:
                    line = line + templine[templine.index('-->') + 3:]
        elif in_comment_block:
            if '-->' in line:
                line = line[line.index('-->') + len('-->'):]
                in_comment_block = False
                if '<!--' in line:
                    line = line[:line.index('<!--')]
                    in_comment_block = True
            else:
                continue
        line = line.strip()
        if line == '':
            continue
        if line.startswith('##'):
            # time to bundle up the previous section's dictionary
            json_dict = {'doc': doc, 'title': cur_section_name, 'content': cur_content.strip() + ' ',
                         'url': base_url_of_course + rel_url, 'relUrl': rel_url}
            list_of_json_dicts.append(json_dict)
            cur_section_name = line[2:].strip()
            cur_content = ''
            rel_url = cur_section_name.lower()
            for char in punctuation:
                if char == '-':
                    continue
                rel_url = rel_url.replace(char, '')
            rel_url = '/#' + rel_url.replace(' ', '-')
        elif cur_section_name == 'Calendar':
            if line[0].isalpha():
                cur_content += line.strip() + ' '
            elif '<table>' in line:
                cur_content = add_calendar_content(cur_content)
        elif len(list_of_json_dicts) == 0:  # we're in the first section
            # just add lines that start with an alpha character OR indicate instructor/TA info
            if line[0].isalpha():
                cur_content += clean_out_formatting(line.strip()) + ' . '
            elif 'site.staffers' in line and "where: 'role', 'Instructor'" in line:
                for staffer_tup in staffer_order:
                    if staffer_tup[1] == 'Instructor':
                        cur_content += get_staff_member_info(staffer_tup[0])
            elif 'site.staffers' in line and "where: 'role', 'Teaching Assistant'" in line:
                for staffer_tup in staffer_order:
                    if staffer_tup[1] == 'Teaching Assistant':
                        cur_content += get_staff_member_info(staffer_tup[0])
        else:
            # figure out how to format bullets, etc.
            if line.startswith('* ') or line.startswith('- '):
                cur_content += '. | ' + clean_out_formatting(line[2:].strip()) + ' | '
            else:
                cur_content += clean_out_formatting(line) + ' '
            pass

json_dict = {'doc': doc, 'title': cur_section_name, 'content': cur_content.strip() + ' ',
                         'url': base_url_of_course + rel_url, 'relUrl': rel_url}
list_of_json_dicts.append(json_dict)
list_of_json_dicts.append({'doc': doc, 'title': doc, 'content': ' ',
                           'url': base_url_of_course + '/', 'relUrl': '/'})
overall_dict_to_jsonify = {}
for i in range(len(list_of_json_dicts)):
    overall_dict_to_jsonify[i] = list_of_json_dicts[i]

with open(fname_to_write_to, 'w') as f:
    json.dump(overall_dict_to_jsonify, f)
print('Wrote ' + fname_to_write_to)
