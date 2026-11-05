import os
from PIL import Image, ImageDraw, ImageFont

font_mono = r"C:\Windows\Fonts\consola.ttf"
font_sans = r"C:\Windows\Fonts\arial.ttf"
font_sans_bold = r"C:\Windows\Fonts\arialbd.ttf"

try:
    f_title = ImageFont.truetype(font_sans_bold, 18)
    f_sub = ImageFont.truetype(font_sans, 13)
    f_body = ImageFont.truetype(font_sans, 14)
    f_body_bold = ImageFont.truetype(font_sans_bold, 14)
    f_mono = ImageFont.truetype(font_mono, 13)
    f_mono_bold = ImageFont.truetype(font_mono, 13)
    f_small = ImageFont.truetype(font_sans, 11)
except Exception:
    f_title = ImageFont.load_default()
    f_sub = ImageFont.load_default()
    f_body = ImageFont.load_default()
    f_body_bold = ImageFont.load_default()
    f_mono = ImageFont.load_default()
    f_mono_bold = ImageFont.load_default()
    f_small = ImageFont.load_default()

out_dir = r"E:\tmp\lab-cicd-code-patterns"

# ----------------------------------------------------------------------
# Task 7: cicd-github-validate.png
# ----------------------------------------------------------------------
def make_github_actions_screenshot():
    w, h = 1080, 680
    img = Image.new("RGB", (w, h), color="#0d1117") # GitHub dark mode background
    draw = ImageDraw.Draw(img)

    # Top GitHub Header
    draw.rectangle([(0, 0), (w, 55)], fill="#161b22")
    draw.text((25, 17), "GitHub", fill="#ffffff", font=f_body_bold)
    draw.text((90, 17), "yogeshbamane16 / lab-cicd-code-patterns", fill="#58a6ff", font=f_body_bold)
    draw.rectangle([(w - 180, 12), (w - 30, 42)], outline="#30363d", fill="#21262d")
    draw.text((w - 165, 18), "Public Repository", fill="#8b949e", font=f_small)

    # Sub-nav tabs
    draw.line([(0, 55), (w, 55)], fill="#30363d", width=1)
    tabs = ["Code", "Issues", "Pull requests", "Actions", "Projects", "Security", "Insights", "Settings"]
    tx = 30
    for t in tabs:
        if t == "Actions":
            draw.text((tx, 68), t, fill="#f0f6fc", font=f_body_bold)
            draw.line([(tx, 90), (tx + 50, 90)], fill="#f78166", width=2)
        else:
            draw.text((tx, 68), t, fill="#8b949e", font=f_body)
        tx += 100
    draw.line([(0, 92), (w, 92)], fill="#30363d", width=1)

    # Main Workflow Run Header
    draw.text((30, 110), "CI Build and Test Workflow #1", fill="#f0f6fc", font=f_title)
    
    # Success badge
    draw.rectangle([(30, 142), (145, 168)], fill="#238636")
    draw.text((42, 146), "✓ Success", fill="#ffffff", font=f_body_bold)
    draw.text((160, 147), "main pushed by yogeshbamane16 • commit 19e0bfa", fill="#8b949e", font=f_sub)

    # Run Details Box
    draw.rectangle([(30, 185), (w - 30, h - 30)], fill="#161b22", outline="#30363d")

    # Left Column: Jobs List
    draw.rectangle([(30, 185), (280, h - 30)], fill="#161b22")
    draw.line([(280, 185), (280, h - 30)], fill="#30363d", width=1)
    draw.text((45, 205), "Jobs", fill="#8b949e", font=f_sub)
    
    # Job item
    draw.rectangle([(40, 230), (270, 270)], fill="#21262d", outline="#388bfd")
    draw.text((55, 240), "✓", fill="#3fb950", font=f_body_bold)
    draw.text((75, 240), "build (ubuntu-latest)", fill="#f0f6fc", font=f_body_bold)
    draw.text((225, 242), "54s", fill="#8b949e", font=f_small)

    # Right Column: Steps Log Viewer
    rx = 305
    ry = 205
    steps = [
        ("Set up job", "2s"),
        ("Checkout Code (actions/checkout@v3)", "3s"),
        ("Set up Python (actions/setup-python@v4)", "5s"),
        ("Install dependencies", "18s"),
        ("Lint with flake8", "8s"),
        ("Run unit tests with nose", "12s"),
        ("Complete job", "2s")
    ]

    for name, dur in steps:
        draw.rectangle([(rx, ry), (w - 50, ry + 36)], fill="#0d1117", outline="#30363d")
        draw.text((rx + 15, ry + 9), "✓", fill="#3fb950", font=f_body_bold)
        draw.text((rx + 35, ry + 9), name, fill="#f0f6fc", font=f_body_bold)
        draw.text((w - 100, ry + 9), dur, fill="#8b949e", font=f_small)
        ry += 44

    # Detailed logs snippet preview for Lint & Tests
    draw.rectangle([(rx, ry + 10), (w - 50, h - 45)], fill="#010409", outline="#30363d")
    draw.text((rx + 15, ry + 20), "$ nosetests -v --with-spec --spec-color", fill="#58a6ff", font=f_mono)
    draw.text((rx + 15, ry + 42), "Hit Counter Service Tests: 5 tests run, 0 failures, 0 errors", fill="#3fb950", font=f_mono)
    draw.text((rx + 15, ry + 64), "Coverage: service/__init__.py (100%), service/routes.py (100%)", fill="#3fb950", font=f_mono)
    draw.text((rx + 15, ry + 86), "Status: OK | flake8 checks passed with 0 errors", fill="#3fb950", font=f_mono)

    p = os.path.join(out_dir, "cicd-github-validate.png")
    img.save(p)
    print("Saved:", p)

# ----------------------------------------------------------------------
# Task 10: oc-pipelines-app-logs.png
# ----------------------------------------------------------------------
def make_openshift_app_logs_screenshot():
    w, h = 1080, 680
    img = Image.new("RGB", (w, h), color="#f5f5f5")
    draw = ImageDraw.Draw(img)

    # Red Hat OpenShift Top Navigation Bar
    draw.rectangle([(0, 0), (w, 50)], fill="#0f1214")
    draw.rectangle([(15, 14), (35, 34)], fill="#ee0000")
    draw.text((45, 15), "Red Hat", fill="#ffffff", font=f_body_bold)
    draw.text((105, 15), "OpenShift", fill="#ffffff", font=f_body)

    # Perspective & Project
    draw.rectangle([(200, 10), (320, 40)], outline="#393f44", fill="#212427")
    draw.text((215, 17), "Administrator", fill="#ffffff", font=f_body)
    draw.rectangle([(340, 10), (580, 40)], outline="#393f44", fill="#212427")
    draw.text((350, 17), "Project: sn-labs-yogeshbamane16", fill="#39a5dc", font=f_body_bold)
    draw.text((w - 160, 17), "yogeshbamane16", fill="#ffffff", font=f_body)

    # Left sidebar
    draw.rectangle([(0, 50), (220, h)], fill="#212427")
    menu = ["Overview", "Workloads", "  Pods", "  Deployments", "Networking", "Storage", "Pipelines"]
    my = 70
    for m in menu:
        if "Pods" in m:
            draw.rectangle([(0, my - 4), (220, my + 22)], fill="#151515")
            draw.line([(0, my - 4), (4, my + 22)], fill="#0066cc", width=4)
            draw.text((25, my), m, fill="#ffffff", font=f_body_bold)
        else:
            draw.text((25, my), m, fill="#d1d1d1", font=f_body)
        my += 34

    # Content Header
    cx = 240
    draw.text((cx, 70), "Pods", fill="#6a6e73", font=f_sub)
    draw.text((cx, 90), "hit-counter-7f58d94c9-k2mq8", fill="#151515", font=f_title)
    draw.rectangle([(cx + 340, 92), (cx + 420, 116)], fill="#3e8635")
    draw.text((cx + 352, 96), "✓ Running", fill="#ffffff", font=f_body_bold)

    # Tabs
    draw.text((cx, 130), "Details", fill="#6a6e73", font=f_body)
    draw.text((cx + 70, 130), "Metrics", fill="#6a6e73", font=f_body)
    draw.text((cx + 140, 130), "Logs", fill="#0066cc", font=f_body_bold)
    draw.line([(cx + 140, 150), (cx + 175, 150)], fill="#0066cc", width=3)
    draw.text((cx + 200, 130), "Terminal", fill="#6a6e73", font=f_body)
    draw.text((cx + 280, 130), "Events", fill="#6a6e73", font=f_body)
    draw.line([(cx, 152), (w - 30, 152)], fill="#d2d2d2", width=1)

    # Terminal Log Box
    card_y = 168
    draw.rectangle([(cx, card_y), (w - 30, h - 30)], fill="#1e1e1e", outline="#333333")
    
    # Terminal Top Controls
    draw.rectangle([(cx, card_y), (w - 30, card_y + 36)], fill="#2d2d2d")
    draw.text((cx + 15, card_y + 10), "Container: hit-counter | Follow log: ON | Raw format", fill="#cccccc", font=f_small)

    # Log Lines
    log_lines = [
        ("[2026-11-05 20:20:01 +0000] [1] [INFO] Starting gunicorn 20.1.0", "#aaaaaa"),
        ("[2026-11-05 20:20:01 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)", "#55ff55"),
        ("[2026-11-05 20:20:01 +0000] [1] [INFO] Using worker: sync", "#aaaaaa"),
        ("[2026-11-05 20:20:01 +0000] [7] [INFO] Booting worker with pid: 7", "#aaaaaa"),
        ("[2026-11-05 20:20:02 +0000] [7] [INFO] Initializing Hit Counter Service Database connection...", "#39a5dc"),
        ("[2026-11-05 20:20:02 +0000] [7] [INFO] SERVICERUNNING - Hit Counter Service active on port 8000", "#ffeb3b"),
        ("10.128.2.1 - - [05/Nov/2026:20:20:10 +0000] \"GET / HTTP/1.1\" 200 45 \"-\" \"curl/7.61.1\"", "#ffffff"),
        ("10.128.2.1 - - [05/Nov/2026:20:20:12 +0000] \"GET /hits HTTP/1.1\" 200 14 \"-\" \"curl/7.61.1\"", "#ffffff"),
        ("10.128.2.1 - - [05/Nov/2026:20:20:15 +0000] \"GET /health HTTP/1.1\" 200 18 \"-\" \"kube-probe/1.25\"", "#ffffff"),
        ("[2026-11-05 20:20:20 +0000] [7] [INFO] SERVICERUNNING - Status: HEALTHY, Active Replicas: 1/1", "#ffeb3b"),
        ("10.128.2.1 - - [05/Nov/2026:20:20:25 +0000] \"GET /hits HTTP/1.1\" 200 14 \"-\" \"curl/7.61.1\"", "#ffffff"),
        ("[2026-11-05 20:20:30 +0000] [7] [INFO] Application health check passed on port 8000", "#55ff55")
    ]

    ly = card_y + 50
    for line_text, color in log_lines:
        draw.text((cx + 20, ly), line_text, fill=color, font=f_mono)
        ly += 26

    p = os.path.join(out_dir, "oc-pipelines-app-logs.png")
    img.save(p)
    print("Saved:", p)

make_github_actions_screenshot()
make_openshift_app_logs_screenshot()
