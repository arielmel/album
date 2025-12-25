import os
import face_recognition

debug = False
def set_debug(flag):
  debug = flag
  
def print_debug(msg):
  if debug:
    print(msg)
    
def load_images_from_directory(directory_path):
    image_paths = []
    valid_extensions = ('.jpg', '.jpeg', '.png')
    if not os.path.isdir(directory_path):
        print_debug(f"Error: Directory '{directory_path}' not found.")
        return []

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(valid_extensions):
            image_paths.append(os.path.join(directory_path, filename))
    print_debug(f"Found {len(image_paths)} image files in '{directory_path}'.")
    return image_paths

def detect_and_encode_faces(image_path):
    face_data = []
    try:
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)

        if not face_locations:
            print_debug(f"No faces found in {image_path}")
            return []

        face_encodings = face_recognition.face_encodings(image, face_locations)

        for face_encoding in face_encodings:
            face_data.append((face_encoding, image_path))
        print_debug(f"Detected and encoded {len(face_encodings)} face(s) in {image_path}")
    except Exception as e:
        print_debug(f"Error processing image {image_path}: {e}")
    return face_data
