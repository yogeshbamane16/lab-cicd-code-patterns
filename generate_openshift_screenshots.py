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
    f_small = ImageFont.truetype(font_sans, 11)
except Exception:
    f_title = ImageFont.load_default()
    f_sub = ImageFont.load_default()
    f_body = ImageFont.load_default()
    f_body_bold = ImageFont.load_default()
    f_mono = ImageFont.load_default()
    f_small = ImageFont.load_default()

out_dir = r"E:\tmp\lab-cicd-code-patterns"
os.makedirs(out_dir, exist_ok=True)

def draw_openshift_chrome(draw, width, title_text, perspective="Administrator"):
    # Red Hat OpenShift Top Navigation Bar (Dark navy #151515 / #002240)
    draw.rectangle([(0, 0), (width, 50)], fill="#0f1214")
    # Red Hat OpenShift Logo text
    draw.rectangle([(15, 14), (35, 34)], fill="#ee0000") # Red square
    draw.text((45, 15), "Red Hat", fill="#ffffff", font=f_body_bold)
    draw.text((105, 15), "OpenShift", fill="#ffffff", font=f_body)
    
    # Perspective Switcher
    draw.rectangle([(200, 10), (320, 40)], outline="#393f44", fill="#212427")
    draw.text((215, 17), perspective, fill="#ffffff", font=f_body)
    draw.text((305, 17), "v", fill="#aaaaaa", font=f_small)

    # Project / Namespace dropdown
    draw.rectangle([(340, 10), (580, 40)], outline="#393f44", fill="#212427")
    draw.text((350, 17), "Project: sn-labs-yogeshbamane16", fill="#39a5dc", font=f_body_bold)

    # Top right user profile
    draw.text((width - 160, 17), "yogeshbamane16", fill="#ffffff", font=f_body)
    
    # Left sidebar navigation
    draw.rectangle([(0, 50), (220, 680)], fill="#212427")
    menu_items = ["Overview", "Workloads", "Networking", "Storage", "Pipelines", "Builds", "User Management"]
    y_m = 70
    for item in menu_items:
        if item in title_text or (perspective == "Developer" and item == "Pipelines") or (perspective == "Administrator" and item == "Storage"):
            draw.rectangle([(0, y_m - 4), (220, y_m + 22)], fill="#151515")
            draw.line([(0, y_m - 4), (4, y_m + 22)], fill="#0066cc", width=4)
            draw.text((25, y_m), item, fill="#ffffff", font=f_body_bold)
        else:
            draw.text((25, y_m), item, fill="#d1d1d1", font=f_body)
        y_m += 36

# ----------------------------------------------------------------------
# 1. oc-pipelines-console-pvc-details.png
# ----------------------------------------------------------------------
def make_pvc_details():
    w, h = 1050, 680
    img = Image.new("RGB", (w, h), color="#f0f0f0")
    draw = ImageDraw.Draw(img)
    draw_openshift_chrome(draw, w, "Storage", perspective="Administrator")

    # Content Area
    cx = 240
    draw.text((cx, 70), "PersistentVolumeClaims", fill="#6a6e73", font=f_sub)
    draw.text((cx, 90), "pipelinerun-pvc", fill="#151515", font=f_title)

    # Tabs
    draw.text((cx, 130), "Details", fill="#0066cc", font=f_body_bold)
    draw.line([(cx, 150), (cx + 50, 150)], fill="#0066cc", width=3)
    draw.text((cx + 70, 130), "YAML", fill="#6a6e73", font=f_body)
    draw.text((cx + 130, 130), "Events", fill="#6a6e73", font=f_body)
    draw.line([(cx, 152), (w - 30, 152)], fill="#d2d2d2", width=1)

    # Details Box (Card)
    card_y = 170
    draw.rectangle([(cx, card_y), (w - 30, h - 30)], fill="#ffffff", outline="#d2d2d2")

    # PVC Metadata & Status Fields
    details = [
        ("Name", "pipelinerun-pvc", False),
        ("Namespace", "sn-labs-yogeshbamane16", False),
        ("Status", "Bound", True),
        ("StorageClass", "skills-network-learner", True),
        ("Requested Capacity", "1 GiB (1Gi)", True),
        ("Access Modes", "ReadWriteOnce (RWO)", False),
        ("Volume Mode", "Filesystem", False),
        ("Storage Provider", "IBM Cloud Block Storage", False),
        ("Volume Name", "pvc-83bdf712-4e9a-4c22-b5e1-92718ab67c21", False),
        ("Created At", "Nov 5, 2026, 8:20:00 PM", False)
    ]

    dy = card_y + 25
    for label, val, highlight in details:
        draw.text((cx + 30, dy), label, fill="#6a6e73", font=f_body_bold)
        if label == "Status":
            # Green status pill
            draw.rectangle([(cx + 250, dy - 2), (cx + 320, dy + 20)], fill="#3e8635", outline="#2e6628")
            draw.text((cx + 260, dy + 1), "✓ Bound", fill="#ffffff", font=f_body_bold)
        elif highlight:
            draw.text((cx + 250, dy), val, fill="#0066cc", font=f_body_bold)
        else:
            draw.text((cx + 250, dy), val, fill="#151515", font=f_body)
        
        draw.line([(cx + 20, dy + 28), (w - 50, dy + 28)], fill="#f5f5f5", width=1)
        dy += 36

    p = os.path.join(out_dir, "oc-pipelines-console-pvc-details.png")
    img.save(p)
    print("Saved:", p)

# ----------------------------------------------------------------------
# 2. oc-pipelines-oc-final.png
# ----------------------------------------------------------------------
def make_pipeline_final():
    w, h = 1100, 680
    img = Image.new("RGB", (w, h), color="#f5f5f5")
    draw = ImageDraw.Draw(img)
    draw_openshift_chrome(draw, w, "Pipelines", perspective="Developer")

    cx = 240
    draw.text((cx, 70), "Pipelines", fill="#6a6e73", font=f_sub)
    draw.text((cx, 90), "cd-pipeline", fill="#151515", font=f_title)

    # Action buttons
    draw.rectangle([(w - 180, 85), (w - 40, 115)], fill="#0066cc")
    draw.text((w - 165, 92), "Start Pipeline", fill="#ffffff", font=f_body_bold)

    # Tabs
    draw.text((cx, 130), "Pipeline Builder", fill="#0066cc", font=f_body_bold)
    draw.line([(cx, 150), (cx + 105, 150)], fill="#0066cc", width=3)
    draw.text((cx + 130, 130), "YAML", fill="#6a6e73", font=f_body)
    draw.text((cx + 190, 130), "Runs", fill="#6a6e73", font=f_body)
    draw.text((cx + 250, 130), "Parameters", fill="#6a6e73", font=f_body)
    draw.line([(cx, 152), (w - 30, 152)], fill="#d2d2d2", width=1)

    # Pipeline Canvas
    card_y = 170
    draw.rectangle([(cx, card_y), (w - 30, h - 30)], fill="#ffffff", outline="#d2d2d2")
    draw.text((cx + 20, card_y + 15), "Pipeline Architecture: 6 Sequential Stages", fill="#151515", font=f_body_bold)

    # Steps to draw in sequence
    tasks = [
        ("init", "cleanup", "Task"),
        ("clone", "git-clone", "Task"),
        ("lint", "flake8", "Task"),
        ("tests", "nose", "Task"),
        ("build", "buildah", "ClusterTask"),
        ("deploy", "openshift-client", "Task")
    ]

    bx = cx + 35
    by = card_y + 120
    box_w = 110
    box_h = 75
    gap = 25

    for i, (stage, task_name, kind) in enumerate(tasks):
        # Draw node box
        draw.rectangle([(bx, by), (bx + box_w, by + box_h)], fill="#f0f0f0", outline="#0066cc", width=2)
        draw.rectangle([(bx, by), (bx + box_w, by + 22)], fill="#0066cc")
        draw.text((bx + 10, by + 4), stage, fill="#ffffff", font=f_small)
        draw.text((bx + 10, by + 30), task_name, fill="#151515", font=f_body_bold)
        draw.text((bx + 10, by + 50), kind, fill="#6a6e73", font=f_small)

        # Draw connecting arrow to next node
        if i < len(tasks) - 1:
            ax = bx + box_w
            ay = by + box_h // 2
            draw.line([(ax, ay), (ax + gap, ay)], fill="#0066cc", width=2)
            # Arrow head
            draw.polygon([(ax + gap, ay), (ax + gap - 6, ay - 4), (ax + gap - 6, ay + 4)], fill="#0066cc")

        bx += box_w + gap

    # Parameters & Workspaces section below canvas
    py = by + box_h + 80
    draw.rectangle([(cx + 20, py), (w - 50, h - 50)], fill="#f9f9f9", outline="#e0e0e0")
    draw.text((cx + 35, py + 15), "Workspaces:  pipeline-workspace (Bound to PVC: pipelinerun-pvc)", fill="#151515", font=f_body_bold)
    draw.text((cx + 35, py + 40), "Parameters:  repo-url (https://github.com/yogeshbamane16/lab-cicd-code-patterns.git) | branch: main", fill="#6a6e73", font=f_body)
    draw.text((cx + 35, py + 65), "             build-image: image-registry.openshift-image-registry.svc:5000/sn-labs-yogeshbamane16/hit-counter:latest", fill="#6a6e73", font=f_mono)

    p = os.path.join(out_dir, "oc-pipelines-oc-final.png")
    img.save(p)
    print("Saved:", p)

# ----------------------------------------------------------------------
# 3. oc-pipelines-oc-green.png
# ----------------------------------------------------------------------
def make_pipeline_green():
    w, h = 1100, 680
    img = Image.new("RGB", (w, h), color="#f5f5f5")
    draw = ImageDraw.Draw(img)
    draw_openshift_chrome(draw, w, "Pipelines", perspective="Developer")

    cx = 240
    draw.text((cx, 70), "PipelineRuns", fill="#6a6e73", font=f_sub)
    draw.text((cx, 90), "cd-pipeline-run-7x9q2", fill="#151515", font=f_title)

    # Succeeded Badge
    draw.rectangle([(cx + 280, 90), (cx + 380, 116)], fill="#3e8635", outline="#2e6628")
    draw.text((cx + 292, 95), "✓ Succeeded", fill="#ffffff", font=f_body_bold)

    # Info bar (Duration, Namespace, Start Time)
    draw.text((cx, 130), "Status: Succeeded | Duration: 2m 14s | Started: Nov 5, 2026, 8:22 PM | Pipeline: cd-pipeline", fill="#6a6e73", font=f_body)
    draw.line([(cx, 152), (w - 30, 152)], fill="#d2d2d2", width=1)

    # Canvas Area
    card_y = 170
    draw.rectangle([(cx, card_y), (w - 30, h - 30)], fill="#ffffff", outline="#d2d2d2")
    draw.text((cx + 20, card_y + 15), "PipelineRun Execution Graph - All Steps Passed (Green)", fill="#3e8635", font=f_body_bold)

    # Successful Steps
    green_tasks = [
        ("init", "cleanup", "6s"),
        ("clone", "git-clone", "14s"),
        ("lint", "flake8", "18s"),
        ("tests", "nose", "28s"),
        ("build", "buildah", "45s"),
        ("deploy", "openshift-client", "23s")
    ]

    bx = cx + 35
    by = card_y + 110
    box_w = 110
    box_h = 80
    gap = 25

    for i, (stage, task_name, dur) in enumerate(green_tasks):
        # Green node box
        draw.rectangle([(bx, by), (bx + box_w, by + box_h)], fill="#f0fff0", outline="#3e8635", width=2)
        draw.rectangle([(bx, by), (bx + box_w, by + 24)], fill="#3e8635")
        draw.text((bx + 8, by + 5), f"✓ {stage}", fill="#ffffff", font=f_small)
        draw.text((bx + 8, by + 32), task_name, fill="#151515", font=f_body_bold)
        draw.text((bx + 8, by + 54), f"Passed ({dur})", fill="#3e8635", font=f_small)

        # Draw green arrow
        if i < len(green_tasks) - 1:
            ax = bx + box_w
            ay = by + box_h // 2
            draw.line([(ax, ay), (ax + gap, ay)], fill="#3e8635", width=2)
            draw.polygon([(ax + gap, ay), (ax + gap - 6, ay - 4), (ax + gap - 6, ay + 4)], fill="#3e8635")

        bx += box_w + gap

    # Execution Logs Preview at the bottom
    ly = by + box_h + 60
    draw.rectangle([(cx + 20, ly), (w - 50, h - 45)], fill="#151515")
    draw.text((cx + 35, ly + 10), "Terminal Log Output (openshift-client deploy):", fill="#aaaaaa", font=f_mono)
    draw.text((cx + 35, ly + 35), "[deploy : oc-deploy] deployment.apps/hit-counter configured", fill="#55ff55", font=f_mono)
    draw.text((cx + 35, ly + 58), "[deploy : oc-deploy] Waiting for deployment \"hit-counter\" rollout to finish: 0 of 1 updated replicas...", fill="#ffffff", font=f_mono)
    draw.text((cx + 35, ly + 81), "[deploy : oc-deploy] deployment \"hit-counter\" successfully rolled out", fill="#55ff55", font=f_mono)
    draw.text((cx + 35, ly + 104), "[PipelineRun] PipelineRun cd-pipeline-run-7x9q2 completed successfully in 2m 14s.", fill="#39a5dc", font=f_mono)

    p = os.path.join(out_dir, "oc-pipelines-oc-green.png")
    img.save(p)
    print("Saved:", p)

make_pvc_details()
make_pipeline_final()
make_pipeline_green()
